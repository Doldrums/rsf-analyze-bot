from typing import List
from sqlalchemy.orm import Session

from ..models.restaurant import Restaurant
from ..schemas.restaurant import RestaurantCreate, RestaurantFull as RestaurantScheme

def get_restaurant(db: Session, by_id: int) -> RestaurantScheme:
    return db.query(Restaurant).filter(Restaurant.id == by_id).first()

def get_restaurants(db: Session, for_owner: int = None) -> List[RestaurantScheme]:
    if for_owner:
        return db.query(Restaurant).filter(Restaurant.owner_id == for_owner).all()

    return db.query(Restaurant).all()

def create_restaurant(db: Session, restaurant: RestaurantCreate) -> RestaurantScheme:
    db_restaurant = Restaurant(
        name=restaurant.name, 
        about=restaurant.about, 
        address=restaurant.address,
        floor_id=restaurant.floor_id, 
        owner_id=restaurant.owner_id,
        archilogic_token=restaurant.archilogic_token
    )
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)

    return db_restaurant
