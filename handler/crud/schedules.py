from typing import List
from sqlalchemy.orm import Session

from ..schemas.schedule import Schedule as ScheduleScheme
from ..models.schedule import Schedule
from ..models.restaurant import Restaurant


def create_schedule(db: Session, for_restaurant: Restaurant, schedules: List[ScheduleScheme]):
    for schedule in schedules:
        db_schedule = Schedule(
            restaurant_id = for_restaurant.id,
            day_of_week = schedule.day_of_week,
            opens_at = schedule.opens_at,
            closes_at = schedule.closes_at,
        )
        db.add(db_schedule)
    
    db.commit()
    db.refresh(for_restaurant)

    return for_restaurant
