"""Сервис сохранения, просмотра и удаления путешествий."""

from datetime import date

from models.treavels import Treavels
from repositories.travel_repository import TravelRepository


class TravelServiceError(Exception):
    """Ошибка работы с путешествиями."""


def _place_line(word: str, place: dict) -> str:
    return f"{word} {place['name']} с ценой {place['price']}$ и сайтом - {place['url']}"


class TravelService:
    """Бизнес-логика работы с путешествиями."""

    def __init__(self, repository: TravelRepository | None = None):
        self._repository = repository or TravelRepository()

    def build_travel_text(self, city: str, date_text: str, hotel: dict, cafe: dict) -> str:
        return (
            "Вы создали путешествие:\n"
            f"Путешествие в {city} на {date_text}:\n"
            f"{_place_line('Отель', hotel)}\n"
            f"{_place_line('Кафе', cafe)}"
        )

    def save_travel(
        self,
        telegram_id: int,
        city: str,
        travel_date: date,
        hotel: dict,
        cafe: dict,
    ) -> Treavels:
        try:
            return self._repository.save(
                telegram_id=telegram_id,
                city=city,
                travel_date=travel_date,
                hotel_text=_place_line("Отель", hotel),
                cafe_text=_place_line("Кафе", cafe),
            )
        except Exception as exc:
            raise TravelServiceError(f"Не удалось сохранить путешествие: {exc}") from exc

    def get_user_travels(self, telegram_id: int) -> list[Treavels]:
        try:
            return self._repository.get_all(telegram_id)
        except Exception as exc:
            raise TravelServiceError(f"Не удалось загрузить путешествия: {exc}") from exc

    def format_saved_travel(self, travel: Treavels) -> str:
        return (
            "Вы создали путешествие:\n"
            f"Путешествие в {travel.city} на {travel.date:%d.%m.%Y}:\n"
            f"{travel.hotel_text}\n"
            f"{travel.cafe_text}"
        )

    def delete_travel(self, telegram_id: int, travel_id: int) -> bool:
        try:
            return self._repository.delete(travel_id, telegram_id)
        except Exception as exc:
            raise TravelServiceError(f"Не удалось удалить путешествие: {exc}") from exc