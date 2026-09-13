"""Сервис поиска кафе и отелей по трём ценовым категориям."""

from api.cafe import CityNotFoundError, Place, PlaceAPI


class SearchPlaceError(Exception):
    """Ошибка поиска мест."""


class SearchPlaceService:
    """Проверяет город и находит кафе/отели через внешний API."""

    def __init__(self, api: PlaceAPI | None = None):
        self._api = api or PlaceAPI()

    def check_city(self, city: str) -> tuple[bool, str]:
        """Возвращает (существует ли город, текст ошибки)."""
        try:
            if not self._api.city_exists(city):
                return False, f"Город «{city}» не найден. Попробуйте ещё раз."
            return True, ""
        except CityNotFoundError as exc:
            return False, str(exc)
        except Exception as exc:
            return False, f"Не удалось проверить город: {exc}"

    def get_cafes(self, city: str) -> list[Place]:
        try:
            return self._api.get_cafes(city)
        except Exception as exc:
            raise SearchPlaceError(f"Не удалось найти кафе: {exc}") from exc

    def get_hotels(self, city: str) -> list[Place]:
        try:
            return self._api.get_hotels(city)
        except Exception as exc:
            raise SearchPlaceError(f"Не удалось найти отель: {exc}") from exc