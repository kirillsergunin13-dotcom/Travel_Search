"""Репозиторий для работы с таблицей путешествий в базе данных."""

from datetime import date
from typing import Optional

from sqlalchemy import select

from models.database import get_session
from models.treavels import Treavels


class TravelRepository:
    """CRUD-операции над путешествиями конкретного пользователя."""

    def __init__(self, session_factory=get_session):
        self._session_factory = session_factory

    def save(
        self,
        telegram_id: int,
        city: str,
        travel_date: date,
        hotel_text: str,
        cafe_text: str,
    ) -> Treavels:
        """Сохраняет новое путешествие и возвращает запись из БД."""
        travel = Treavels(
            telegram_id=telegram_id,
            city=city,
            date=travel_date,
            hotel_text=hotel_text,
            cafe_text=cafe_text,
        )
        with self._session_factory() as session:
            session.add(travel)
            session.commit()
            session.refresh(travel)
            return travel

    def get_all(self, telegram_id: int) -> list[Treavels]:
        """Возвращает путешествия пользователя от старых к новым."""
        with self._session_factory() as session:
            stmt = (
                select(Treavels)
                .where(Treavels.telegram_id == telegram_id)
                .order_by(Treavels.date.asc(), Treavels.id.asc())
            )
            return list(session.scalars(stmt))

    def get_by_id(self, travel_id: int, telegram_id: int) -> Optional[Treavels]:
        with self._session_factory() as session:
            stmt = select(Treavels).where(
                Treavels.id == travel_id,
                Treavels.telegram_id == telegram_id,
            )
            return session.scalar(stmt)

    def delete(self, travel_id: int, telegram_id: int) -> bool:
        """Удаляет путешествие и возвращает True при успехе."""
        travel = self.get_by_id(travel_id, telegram_id)
        if travel is None:
            return False
        with self._session_factory() as session:
            session.delete(travel)
            session.commit()
            return True