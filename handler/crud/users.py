import bcrypt
from sqlalchemy import update
from sqlalchemy.orm import Session

from ..models.user import User
from ..schemas.user import UserCreate, User as UserScheme, UserUpdate

def get_user(db: Session, by_email: str = None, by_id: int = None) -> UserScheme:
    query = db.query(User)
    
    if by_email:
        query = query.filter(User.email == by_email)
    elif by_id:
        query = query.filter(User.id == by_id)

    return query.first()


def update_user(db: Session, id: int, data: UserUpdate) -> UserScheme:
    db.query(User).filter(User.id == id).update(data.dict(exclude_none = True))
    db.commit()

    return db.query(User).get(id)

def create_user(db: Session, user: UserCreate) -> UserScheme:
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    db_user = User(email=user.email, name=user.name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
