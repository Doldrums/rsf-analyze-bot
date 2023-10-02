# from base import Base
# from sqlalchemy import Column, Integer, String

# class Repo(Base):
#     __tablename__ = 'repos'

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String)
#     repo_url = Column(String)
#     issue_id = Column(String)
#     data = Column(String)


from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from db import Base


class Repo(Base):
    __tablename__ = 'repos'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    repo_url = Column(String)
    issue_id = Column(String)
    installation_token = Column(String)
    data = Column(String)
