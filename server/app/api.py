from datetime import timedelta
from typing import List
from fastapi.responses import FileResponse
from fastapi import FastAPI, Body, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status
from . import models, schemas, crud
from .database import engine, SessionLocal
from .auth import auth
from .auth import token_generator

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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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


# User

@app.post("/token", response_model=token_generator.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db=db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=token_generator.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token_generator.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/", response_model=List[schemas.User], tags=["users"])
async def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    db_users = crud.get_users(db=db, skip=skip, limit=limit)
    if len(db_users) == 0:
        raise HTTPException(status_code=400, detail="List is Empty")
    return db_users


@app.get("/users/{user_id}", response_model=schemas.User, tags=["users"])
async def get_user(user_id, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user:
        return db_user


@app.post("/users/", response_model=schemas.User, tags=["users"])
def post_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User Already Exist!")
    return crud.create_user(db=db, user=user)


@app.post("/users/{user_id}/", tags=["users"])
async def post_coffee_to_user(user_email: str, coffee_name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found!")
    db_coffee = crud.get_coffee_by_name(db=db, coffee_name=coffee_name)
    if db_coffee is None:
        raise HTTPException(status_code=404, detail="Coffee Not Found!")
    return HTTPException(status_code=200, detail="Added Successfully")


@app.put("/users/{user_id}", response_model=schemas.User, tags=["users"])
async def put_user(user_id: int, username: str = "", full_name: str = "",
                   db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, username=username, full_name=full_name)


@app.get("/users/{user_id}/coffee/", tags=["users"])
async def get_user_coffee(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(user_id=user_id, db=db)
    if db_user:
        return crud.get_user_coffee(user_id=user_id, db=db)
    raise HTTPException(status_code=404, detail="User Not Found!")


# Coffee

@app.get("/coffee/", response_model=List[schemas.Coffee], tags=["coffee"])
async def get_coffee(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_coffee = crud.get_coffee(db=db, limit=limit, skip=skip)
    if len(db_coffee) != 0:
        return db_coffee
    raise HTTPException(status_code=400, detail="Coffee List is Empty!")


@app.get("/coffee/{coffee_name}/image/", tags=["coffee"])
async def get_coffee_image(coffee_name: str, db: Session = Depends(get_db)):
    coffee = crud.get_coffee_by_name(db=db, coffee_name=coffee_name)
    return FileResponse(coffee.img)


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
