from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base

from .image import Image as _
from .review import Review as _
from .schedule import Schedule as _

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String, nullable=False)
    about = Column(String)
    floor_id = Column(String)
    archilogic_token = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='owned_restaurants')
    reservations = relationship('Reservation', back_populates='restaurant')
    images = relationship('Image')
    reviews = relationship('Review')
    schedules = relationship('Schedule')
