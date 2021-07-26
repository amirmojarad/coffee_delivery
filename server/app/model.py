from pydantic import BaseModel, Field
from typing import Optional, List


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