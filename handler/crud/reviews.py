from typing import List
from sqlalchemy.orm import Session

from ..schemas.review import ReviewCreate, Review as ReviewScheme
from ..models.review import Review

def get_reviews(db: Session, for_user: int = None, for_restaurant: int = None) -> List[ReviewScheme]:
    query = db.query(Review)
    
    if for_user:
        query = query.filter(Review.author_id == for_user)
    if for_restaurant:
        query = query.filter(Review.restaurant_id == for_restaurant)
    
    return query.all()

def create_review(db: Session, review: ReviewCreate) -> ReviewScheme:
    db_review = Review(
        review=review.review,
        rating=review.rating,
        restaurant_id=review.restaurant_id,
        author_id=review.author_id,
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)

    return db_review
