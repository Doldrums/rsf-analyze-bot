from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from ..database import Base
from ..schemas.schedule import DayOfWeek


class Schedule(Base):
    __tablename__ = 'schedules'

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), primary_key=True)
    day_of_week = Column(Enum(DayOfWeek), primary_key=True)
    opens_at = Column(Integer, nullable=False)
    closes_at = Column(Integer, nullable=False)
