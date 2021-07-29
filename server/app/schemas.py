from typing import List
from pydantic import BaseModel


class CoffeeBase(BaseModel):
    name: str


class CoffeeCreate(CoffeeBase):
    # ingredients: List[str]
    caffeine: float
    calories: float
    cholesterol: float

    class Config:
        schema_extra = {
            "example": {
                "name": "Americano",
                "caffeine": 0.0,
                "calories": 0.0,
                "cholesterol": 0.0,
                # "ingredients": []
            }
        }


class Coffee(CoffeeCreate):
    id: int
    sodium: float
    protein: float
    dietary_fiber: float
    sugars: float
    saturated_fat: float
    total_fat: float
    total_carbohydrates: float

    class Config:
        orm_mode = True


class CoffeeItem(CoffeeBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    username: str
    hashed_password: str
    full_name: str
    is_active: bool
    items: List[str] = []

    class Config:
        orm_mode = True
