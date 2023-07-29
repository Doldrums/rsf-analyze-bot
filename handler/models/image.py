from sqlalchemy import Column, ForeignKey, Integer, String

from ..database import Base


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, index=True)
    path = Column(String)

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
