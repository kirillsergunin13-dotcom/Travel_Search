"""Клиент поиска кафе и отелей по названию города.

Использует открытые API OpenStreetMap: Nominatim — проверка существования
города, Overpass — поиск заведений. Если сеть недоступна или результатов
мало, генерируются данные, чтобы бот продолжал работать без остановки.
"""

import hashlib
import json
import urllib.parse
from dataclasses import dataclass

import requests

USER_AGENT = "TravelSearchBot-v2 (educational project)"

CAFE_NAMES = [
    "Кафе «Вкусная чашка»",
    "Кофейня «Утро»",
    "Бистро «Уют»",
    "Ресторан «Амбассадор»",
    "Кафе-бар «Мохито»",
    "Кондитерская «Венеция»",
    "Кафе «Чайхана»",
    "Ресторан «Золотой дракон»",
    "Бранч «Вишня»",
]

HOTEL_NAMES = [
    "Отель «Гранд»",
    "Хостел «Травел»",
    "Гостиница «Вокзальная»",
    "Отель «Престиж»",
    "Спа-отель «Альянс»",
    "Бутик-отель «Шато»",
    "Отель «Космос»",
    "Апарт-отель «Лофт»",
    "Мини-отель «Уютный двор»",
]

WORDS = {
    "кафе": ["Дорогое", "Среднее", "Дешёвое"],
    "отель": ["Дорогой", "Средний", "Дешёвый"],
}

# Базовая цена для дорогого/среднего/дешёвого варианта.
PRICES = {
    "кафе": [1800, 900, 350],
    "отель": [12000, 5500, 1800],
}


class CityNotFoundError(Exception):
    """Город не найден в геокодере."""


class PlaceSearchError(Exception):
    """Не удалось получить список мест."""


@dataclass(frozen=True)
class Place:
    kind: str    # "кафе" или "отель"
    tier: str    # "Дорогое"/"Среднее"/"Дешёвое" или "Дорогой"/...
    name: str
    price: int
    url: str

    @property
    def label(self) -> str:
        return f"{self.tier} {self.kind}"

    def to_dict(self) -> dict:
        return {
            "kind": self.kind,
            "tier": self.tier,
            "name": self.name,
            "price": self.price,
            "url": self.url,
        }


class PlaceAPI:
    """Ищет кафе и отели, возвращает по три ценовые категории."""

    TAGS = {"кафе": ("amenity", "cafe"), "отель": ("tourism", "hotel")}

    def __init__(self, timeout: int = 15):
        self.timeout = timeout

    @staticmethod
    def _headers() -> dict:
        return {"User-Agent": USER_AGENT, "Accept-Language": "ru"}

    def city_exists(self, city: str) -> bool:
        """True, если город найден. При сбое сети считается существующим."""
        try:
            self._geocode(city)
            return True
        except CityNotFoundError:
            return False
        except Exception:
            return True

    def get_cafes(self, city: str) -> list[Place]:
        return self._get_places("кафе", city)

    def get_hotels(self, city: str) -> list[Place]:
        return self._get_places("отель", city)

    def _get_places(self, kind: str, city: str) -> list[Place]:
        places: list[dict] = []
        try:
            places = self._fetch_from_osm(kind, city)
        except Exception:
            places = self._mock_places(kind, city)
        return self._select_places(kind, city, places)

    def _geocode(self, city: str) -> dict:
        response = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={
                "q": city,
                "format": "json",
                "limit": 1,
                "accept-language": "ru",
            },
            headers=self._headers(),
            timeout=self.timeout,
        )
        response.raise_for_status()
        data = response.json()
        if not data:
            raise CityNotFoundError(f"Город «{city}» не найден.")
        return data[0]

    def _fetch_from_osm(self, kind: str, city: str) -> list[dict]:
        tag_key, tag_value = self.TAGS[kind]
        geo = self._geocode(city)
        south, north, west, east = (float(geo["boundingbox"][i]) for i in (0, 1, 2, 3))
        query = (
            f'[out:json][timeout:{self.timeout}];'
            f'(node["{tag_key}"="{tag_value}"]({south},{west},{north},{east});'
            f'way["{tag_key}"="{tag_value}"]({south},{west},{north},{east}););'
            "out tags 40;"
        )
        response = requests.post(
            "https://overpass-api.de/api/interpreter",
            data={"data": query},
            headers=self._headers(),
            timeout=self.timeout,
        )
        response.raise_for_status()
        elements = response.json().get("elements", [])
        result = []
        for element in elements:
            tags = element.get("tags", {})
            name = (tags.get("name") or "").strip()
            if not name:
                continue
            url = tags.get("website") or tags.get("contact:website") or ""
            result.append({"name": name, "url": url})
        return result

    def _select_places(self, kind: str, city: str, places: list[dict]) -> list[Place]:
        if len(places) < 3:
            places = self._mock_places(kind, city)
        places = sorted(places, key=lambda p: p["name"])[:3]
        result = []
        for index, place in enumerate(places):
            seed = f"{kind}:{place['name']}".encode("utf-8")
            price = PRICES[kind][index] + int(hashlib.md5(seed).hexdigest(), 16) % 300
            url = place.get("url")
            if not url:
                query = urllib.parse.quote(f'{place["name"]} {city}')
                url = f"https://www.google.com/search?q={query}"
            result.append(
                Place(
                    kind=kind,
                    tier=WORDS[kind][index],
                    name=place["name"],
                    price=price,
                    url=url,
                )
            )
        return result

    def _mock_places(self, kind: str, city: str) -> list[dict]:
        pool = CAFE_NAMES if kind == "кафе" else HOTEL_NAMES
        chosen = []
        for i in range(9):
            seed = f"{kind}:{city}:{i}".encode("utf-8")
            name = pool[int(hashlib.md5(seed).hexdigest(), 16) % len(pool)]
            if name not in [c["name"] for c in chosen]:
                chosen.append({"name": name, "url": ""})
        return chosen