import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Coffee

file = open('coffee_list.json')
data = json.load(file)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

for item in data["coffee_list"]:
    coffee = Coffee()
    coffee.sugars = item["sugars"]
    coffee.sodium = item["sodium"]
    coffee.total_fat = item["total_fat"]
    coffee.total_carbohydrates = item["total_carbohydrates"]
    coffee.saturated_fat = item["saturated_fat"]
    coffee.protein = item["protein"]
    coffee.cholesterol = item["cholesterol"]
    coffee.name = item["name"]
    coffee.caffeine = item["caffeine"]
    coffee.dietary_fiber = item["dietary_fiber"]
    coffee.calories = item["calories"]
    coffee.img = item["img"]
    db.add(coffee)
    db.commit()
    db.refresh(coffee)

db.close()