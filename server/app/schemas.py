from pydantic import BaseModel


class CoffeeBase(BaseModel):
    name: str


class CoffeeCreate(CoffeeBase):
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
            }
        }


class Coffee(CoffeeCreate):
    id: int
    img = str
    sodium: float
    protein: float
    dietary_fiber: float
    sugars: float
    saturated_fat: float
    total_fat: float
    total_carbohydrates: float

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    hashed_password: str
    full_name: str
    is_active: bool
    email: str

    class Config:
        orm_mode = True
