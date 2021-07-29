from typing import List

from fastapi import FastAPI, Body, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status
from . import models, schemas, crud
from .database import engine, SessionLocal
from app.models import Coffee, User

tags_metadata = [
    {
        "name": "root",
        "description": "Root of Project",
    },
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "coffee",
        "description": "Manage coffees",
    },
    {
        "name": "purchase",
        "description": "Purchase Coffee, Involve User and Coffee list"
    }
]

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Coffee Delivery Project", description="Purchase, Show Coffee List, etc!", version="0.1.0",
              tags_metadata=tags_metadata)

def assign_coffee_to_users(user_id: int, coffee_name: str):
    crud.get




# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def get_root():
    return HTTPException(status_code=200, detail="Welcome!")


@app.get("/users/", response_model=List[schemas.User], tags=["users"])
async def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    db_users = crud.get_users(db=db, skip=skip, limit=limit)
    if len(db_users) == 0:
        raise HTTPException(status_code=400, detail="List is Empty")
    return db_users


@app.get("/users/{user_id}", response_model=schemas.User, tags=["users"])
async def get_user(user_id, db: Session = Depends(get_db)):



@app.post("/users/", response_model=schemas.User, tags=["users"])
async


def post_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User Already Exist!")
    return crud.create_user(db=db, user=user)


@app.post("/users/{user_id}/", response_model=schemas.User, tags=["users"])
async def post_coffee_to_user(user_id: int, coffee_name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user:
        raise HTTPException(status_code=404, detail="User Not Found!")
    db_coffee = crud.get_coffee_by_name(db=db, coffee_name=coffee_name)
    if db_coffee:
        raise HTTPException(status_code=404, detail="Coffee Not Found!")


@app.put("/users/{user_id}", response_model=schemas.User, tags=["users"])
async def put_user(user_id: int, username: str = "", full_name: str = "",
                   db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, username=username, full_name=full_name)


@app.get("/coffee/", response_model=List[schemas.Coffee], tags=["coffee"])
async def get_coffee(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_coffee = crud.get_coffee(db=db, limit=limit, skip=skip)
    if len(db_coffee) != 0:
        return db_coffee
    raise HTTPException(status_code=400, detail="Coffee List is Empty!")


@app.post("/coffee/", response_model=schemas.Coffee, tags=["coffee"])
async def post_coffee(coffee: schemas.CoffeeCreate, db: Session = Depends(get_db)):
    db_user = crud.get_coffee_by_name(db, coffee_name=coffee.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Coffee Already Exist!")
    return crud.create_coffee(db=db, coffee=coffee)


@app.put("/coffee/{coffee_name}", response_model=schemas.Coffee, tags=["coffee"])
async def put_coffee(coffee_name: str, db: Session = Depends(get_db), caffeine: float = 0.0, calories: float = 0.0,
                     cholesterol: float = 0.0,
                     sodium: float = 0.0, protein: float = 0.0,
                     dietary_fiber: float = 0.0,
                     sugars: float = 0.0,
                     saturated_fat: float = 0.0,
                     total_fat: float = 0.0,
                     total_carbohydrates: float = 0.0,
                     ingredients: List[str] = []):
    return crud.update_coffee(coffee_name=coffee_name, db=db, caffeine=caffeine, calories=calories,
                              cholesterol=cholesterol,
                              sodium=sodium, protein=protein,
                              dietary_fiber=dietary_fiber,
                              sugars=sugars,
                              saturated_fat=saturated_fat,
                              total_fat=total_fat,
                              total_carbohydrates=total_carbohydrates,
                              ingredients=ingredients)

# @app.post("/coffee/", response_model=schemas.Coffee, tags=["coffee"])
# async def post_coffee(coffee: schemas.CoffeeCreate, db: Session = Depends(get_db)):
#     db_coffee = crud.get_coffee_by_name(db=db, coffee_name=coffee.name)
#     if db_coffee:
#         raise HTTPException(status_code=400, detail="Coffee Already Exist!")
#     return crud.create_coffee(db=db, coffee=coffee)

# @app.post("")


# @app.get("/coffee/")

# @app.post("/users/{user_id}/coffee", response_model=schemas.Coffee)
# async def post_coffee_for_user()

#
# @app.post("/users/", response_model=schemas.User, tags=["users"])
# async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email Already Registered")
#     return crud.create_user(db=db, user=user)
#
#
# @app.get("/users/", response_model=schemas.User, tags=["users"])
# async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     if len(users) == 0:
#         raise HTTPException(status_code=400, detail="List is Empty")
#     return users
#
#
# @app.get("/users/{user_id}", response_model=List[schemas.User], tags=["users"])
# async def get_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db=db, user_id=user_id)
#     if db_user:
#         return db_user
#     raise HTTPException(status_code=404, detail="User not Found!")
#
#
# @app.post("/users/{user_id}/coffee", response_model=schemas.Coffee)
# async def create_coffee_for_user(user_id: int, coffee: schemas.CoffeeCreate, db: Session = Depends(get_db)):
#     return crud.create_user_coffee(db=db, coffee=coffee, user_id=user_id)
#
#
# @app.get("/users/{user_id}/coffee", response_model=schemas.Coffee, tags=["user"])
# async def get_user_coffee(user_id: int, db: Session = Depends(get_db)):
#     user = get_user(user_id=user_id, db=db)
#     if user:
#         return crud.get_user_coffee(db=db, user_id=user_id)
#     raise HTTPException(status_code=404, detail="User Not Found!")

# @app.get("/coffee", response_model=schemas.Coffee, tags=["coffee"])
# async def get_all_coffee(db: Session = get_db, skip: int = 0, limit: int = 100):
#     return crud.get_coffee(db=db, limit=limit, skip=skip)
#

# # fake_users_db = {
# #     "johndoe": {
# #         "username": "johndoe",
# #         "full_name": "John Doe",
# #         "email": "johndoe@example.com",
# #         "hashed_password": "fakehashedsecret",
# #         "disabled": False,
# #     },
# #     "alice": {
# #         "username": "alice",
# #         "full_name": "Alice Wonderson",
# #         "email": "alice@example.com",
# #         "hashed_password": "fakehashedsecret2",
# #         "disabled": True,
# #     },
# # }
# #
# # coffee_list = [
# #     {
# #         "id": 1,
# #         "name": "Americano",
# #         "caffeine": 255.0,
# #         "ingredients": ["Water", "Brewed Espresso"]
# #     },
# #     {
# #         "id": 3,
# #         "name": "temp",
# #         "caffeine": 255.0,
# #         "ingredients": ["Water", "Brewed Espresso"]
# #     },
# #     {
# #         "id": 4,
# #         "name": "liam",
# #         "caffeine": 255.0,
# #         "ingredients": ["Water", "Brewed Espresso"]
# #     }
# # ]
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
#
# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
#
#
# def fake_decode_token(token):
#     # This doesn't provide any security at all
#     # Check the next version
#     user = get_user(coffee_list, token)
#     return user
#
#
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     user = fake_decode_token(token)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return user
#
#
# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user
#
#
# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user_dict = fake_users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#
#     return {"access_token": user.username, "token_type": "bearer"}
#
#
# @app.get("/users/me")
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user
#
#
# @app.get("/", tags=["root"])
# async def get_root() -> dict:
#     return {
#         "message": "Welcome To Coffee Delivery"
#     }
#
#
# @app.get("/coffee_list/all", tags=["coffeeList"])
# async def get_coffee_list() -> dict:
#     return {
#         "data": coffee_list
#     }
#
#
# @app.post("/coffee_list", tags=["coffeeList"])
# async def add_coffee(coffee: Coffee = Body(...)) -> dict:
#     coffee.id = len(coffee_list) + 1
#     coffee_list.append(coffee.dict())
#     return {
#         "status": "Coffee {} Added Successfully".format(coffee.name)
#     }
#
#
# @app.get("/coffee_list/{name}", tags=["coffeeList"])
# async def get_coffee_by_name(name: str) -> dict:
#     response = {}
#     if len(coffee_list) == 0:
#         raise HTTPException(status_code=200, detail="Coffee List is Empty")
#     for coffee in coffee_list:
#         if coffee["name"] == name:
#             response.update({
#                 "status": {
#                     "data": [coffee]
#                 }
#             }
#             )
#             return response
#     raise HTTPException(status_code=404, detail="Coffee with name {} not Found!".format(name))
