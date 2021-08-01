import hashlib
import uuid

from sqlalchemy.orm import Session
from . import models
from .auth import password_hashing

"""
CRUD = Create, Read, Update, Delete
"""

# Update

"""
By creating functions that are only dedicated to interacting with the database 
(get a user or an item) independent of your path operation function,
you can more easily reuse them in multiple parts and also add unit tests for them.
"""


def update_user(db: Session, username: str, full_name: str = "", access_token: str = "", email: str = ""):
    user = db.query(models.User).filter(models.User.username == username).first()
    user.full_name = user.full_name if full_name == "" else full_name
    user.access_token = user.access_token if access_token == "" else access_token
    user.email = user.email if email == "" else email
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_coffee(db: Session, coffee_name: str,
                  sodium: float = 0.0, protein: float = 0.0,
                  dietary_fiber: float = 0.0,
                  sugars: float = 0.0,
                  saturated_fat: float = 0.0,
                  total_fat: float = 0.0,
                  total_carbohydrates: float = 0.0,
                  ):
    coffee = db.query(models.Coffee).filter(models.Coffee.name == coffee_name).first()
    coffee.sodium = sodium if sodium != 0.0 else coffee.sodium
    coffee.protein = protein if protein != 0.0 else coffee.protein
    coffee.dietary_fiber = dietary_fiber if dietary_fiber != 0.0 else coffee.dietary_fiber
    coffee.sugars = sugars if sugars != 0.0 else coffee.sugars
    coffee.saturated_fat = saturated_fat if saturated_fat != 0.0 else coffee.saturated_fat
    coffee.total_fat = total_fat if total_fat != 0.0 else coffee.total_fat
    coffee.total_carbohydrates = total_carbohydrates if total_carbohydrates != 0.0 else coffee.total_carbohydrates
    db.add(coffee)
    db.commit()
    db.refresh(coffee)
    return coffee


# Read


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_coffee(db: Session, user_id: int):
    return db.query(models.Coffee).filter(models.Purchase.user_id == user_id).filter(
        models.Purchase.coffee_id == models.Coffee.id).all()


def get_coffee_by_name(db: Session, coffee_name: str):
    return db.query(models.Coffee).filter(models.Coffee.name == coffee_name).first()


def get_coffee(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Coffee).offset(skip).limit(limit).all()


# Create

def create_user(db: Session, username: str, password: str):
    hashed_password = password_hashing.generate_hash_password(password)
    db_user = models.User(username=username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_purchase(db: Session, user_id: int, coffee_id: int):
    db_purchase = models.Purchase(user_id=user_id, coffee_id=coffee_id)
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase


# utils functions
def hash_password(password: str):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    return hashed_password
