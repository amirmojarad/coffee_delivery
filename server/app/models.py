from sqlalchemy import Integer, String, Boolean, Float, ForeignKey, INTEGER
from sqlalchemy import Column
from sqlalchemy.orm import relationship

from .database import Base


# Entity

class Coffee(Base):
    __tablename__ = "coffee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    caffeine = Column(Float, default=0.0)
    calories = Column(Float, default=0.0)
    cholesterol = Column(Float, default=0.0)
    sodium = Column(Float, default=0.0)
    protein = Column(Float, default=0.0)
    dietary_fiber = Column(Float, default=0.0)
    sugars = Column(Float, default=0.0)
    saturated_fat = Column(Float, default=0.0)
    total_fat = Column(Float, default=0.0)
    total_carbohydrates = Column(Float, default=0.0)
    img = Column(String, unique=True, default="")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    full_name = Column(String, default="")
    username = Column(String, unique=True)
    access_token = Column(String, unique=True)


# Relationships

class Purchase(Base):
    __tablename__ = "purchase"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    coffee_id = Column(Integer, ForeignKey("coffee.id"))
