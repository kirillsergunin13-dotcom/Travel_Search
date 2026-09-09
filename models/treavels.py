from datetime import date

from sqlalchemy import BigInteger, Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from repositories.database import Base

class Treavels(Base):
    __tablename__="treavels"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    city:Mapped[str]= mapped_column(String,nullable=False )
    date:Mapped[date]=mapped_column(date,nullable=False)
    hotel_text:Mapped[str]=mapped_column(String,nullable==False)
    cafe_text:Mapped[str]=mapped_column(String,nullable=False)