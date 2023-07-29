from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base
from .reservation import Reservation
from .restaurant import Restaurant


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    phone = Column(String)
    hashed_password = Column(String)
    archilogic_secret_token = Column(String)
    archilogic_public_token = Column(String)
    is_admin = Column(Boolean, default=False)

    reservations = relationship('Reservation', back_populates='guest')
    owned_restaurants = relationship('Restaurant', back_populates='owner')
