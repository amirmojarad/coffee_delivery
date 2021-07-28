from pydantic import BaseModel, Field
from typing import Optional, List

from sqlalchemy import Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.testing.schema import Column
from sqlalchemy.orm import relationship

from .database import Base


class Coffee(BaseModel):
    id: Optional[int]
    name: str = Field(...)
    caffeine: Optional[float]
    ingredients: Optional[List[str]]
    calories: Optional[Float]
    cholesterol: Optional[Float]
    sodium: Optional[Float]
    protein: Optional[Float]
    dietary_fiber: Optional[Float]
    sugars: Optional[Float]
    saturated_fat: Optional[Float]
    total_fat: Optional[Float]
    total_carbohydrates: Optional[Float]

    class Config:
        schema_extra = {
            "example": {
                "name": "Americano",
            }
        }


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class DBCoffee(Base):
    __tablename__ = "coffee"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    caffeine = Column(Float, index=True)
    ingredients = relationship("DBIngredient", back_populates="coffee")
     

class DBIngredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    coffee_id = Column(Integer, ForeignKey("coffee.id"))
    coffee = relationship("DBCoffee", back_populates="ingredients")


class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
