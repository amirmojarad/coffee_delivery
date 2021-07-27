from pydantic import BaseModel, Field
from typing import Optional, List


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class Coffee(BaseModel):
    id: Optional[int]
    name: str = Field(...)
    caffeine: Optional[float]
    ingredients: Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "name": "Americano",
            }
        }
