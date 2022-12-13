import os
from datetime import datetime
from typing import Dict, List, Optional
from sqlmodel import Field, SQLModel, select
from sqlalchemy import UniqueConstraint, String, Column




# print("sucessfull 1 ")

class User(SQLModel, table=True):

    __tablename__ = "user"

    id: int = Field(primary_key=True)
    name: str
    hashed_password: str
    email: str = Field(sa_column=Column("email", String(40), unique=True))
    is_varified: bool = Field(default=False)
    role_name: str = Field(default=None, foreign_key="role.name")

print("sucessfull 2")

   
class Role(SQLModel, table=True):

    __tablename__ = "role"
    id: int = Field(primary_key=True)
    name: str= Field(sa_column=Column("name", String(40), unique=True))


class Auction(SQLModel, table=True):
    __tablename__ = "auction"

    id: int = Field(primary_key=True)
    title:str = Field(sa_column=Column("title", String(40), unique=True))
    start_time: datetime = Field(default_factory=datetime.utcnow(), nullable=False)
    end_time: datetime = Field(default_factory=datetime.utcnow(), nullable=False)
    start_amount: float
    current_top_bid: float = Field(default=0.0)
    discription: str


print("sucessfull 3")


class UserBid(SQLModel, table=True):    
    __tablename__ = "userbid"
    id: int = Field(primary_key=True)
    auction_id: int = Field(default=None, foreign_key="auction.id")
    user_email: str = Field(default=None, foreign_key="user.email")
    bid_amount: float 


print("sucessfull import ")