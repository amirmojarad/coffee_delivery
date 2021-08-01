from datetime import timedelta
from fastapi.responses import FileResponse
<<<<<<< HEAD
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas, crud
from .database import engine, SessionLocal
=======
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal
from .auth import auth
from .auth import token_generator
>>>>>>> dev

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

<<<<<<< HEAD
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
=======
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
>>>>>>> dev


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


<<<<<<< HEAD
# @app.get("/images/")
# async def download_files_stream():
#     return FileResponse("files/1.jpg")
#

@app.get("/")
async def get_root():
    return HTTPException(status_code=200, detail="Welcome!")


=======
>>>>>>> dev
# User

@app.post("/users/sign_up", tags=["users"])
async def users_sign_up(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(username=form_data.username, db=db, password=form_data.password)
    if user:
        raise HTTPException(status_code=400, detail="User Already Exist")
    new_user = crud.create_user(db=db, username=form_data.username, password=form_data.password)
    access_token_expires = timedelta(minutes=token_generator.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token_generator.create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    new_user.access_token = access_token
    return crud.update_user(db=db, username=new_user.username, access_token=access_token)


@app.get("/users/", tags=["users"])
async def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    db_users = crud.get_users(db=db, skip=skip, limit=limit)
    if len(db_users) == 0:
        raise HTTPException(status_code=400, detail="List is Empty")
    return db_users


@app.get("/users/{username}", tags=["users"], )
async def get_user(username: str, db: Session = Depends(get_db), token: str = Header(None)):
    db_user = crud.get_user_by_username(db=db, username=username)
    if db_user.access_token != token:
        raise HTTPException(status_code=401, detail="Not Authorized")
    if db_user:
        return db_user


@app.put("/users/{user_id}", response_model=schemas.User, tags=["users"])
async def put_user(username: str, full_name: str = "",
                   token: str = Header(None),
                   email: str = "",
                   db: Session = Depends(get_db)):
    user = crud.get_user_by_username(username=username, db=db)
    if user:
        if user.access_token != token:
            raise HTTPException(status_code=401, detail="Not Authorized")
        return crud.update_user(db=db, username=username, full_name=full_name, email=email)
    raise HTTPException(status_code=404, detail="User Not Found")


@app.get("/users/{username}/coffee/", tags=["users"])
async def get_user_coffee(username: str, db: Session = Depends(get_db), token: str = Header(None)):
    db_user = crud.get_user_by_username(username=username, db=db)
    if db_user:
        if db_user.access_token == token:
            return crud.get_user_coffee(user_id=db_user.id, db=db)
        raise HTTPException(status_code=401, detail="Not Authorized")
    raise HTTPException(status_code=404, detail="User Not Found!")


@app.post("/users/{username}/", tags=["users"])
async def post_coffee_to_user(username: str, coffee_name: str, db: Session = Depends(get_db),
                              token: str = Header(None)):
    db_user = crud.get_user_by_username(db=db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found!")
    if db_user.access_token != token:
        raise HTTPException(status_code=401, detail="Not Authorized")
    db_coffee = crud.get_coffee_by_name(db=db, coffee_name=coffee_name)
    if db_coffee is None:
        raise HTTPException(status_code=404, detail="Coffee Not Found!")
    crud.create_purchase(db=db, user_id=db_user.id, coffee_id=db_coffee.id)
    return HTTPException(status_code=200, detail="Added Successfully")


# Coffee

@app.get("/coffee/", tags=["coffee"])
async def get_coffee(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_coffee = crud.get_coffee(db=db, limit=limit, skip=skip)
    if len(db_coffee) != 0:
        return db_coffee
    raise HTTPException(status_code=400, detail="Coffee List is Empty!")


@app.get("/coffee/{coffee_name}/image/", tags=["coffee"])
async def get_coffee_image(coffee_name: str, db: Session = Depends(get_db)):
    coffee = crud.get_coffee_by_name(db=db, coffee_name=coffee_name)
    print(coffee.img)
    return FileResponse(coffee.img)
<<<<<<< HEAD


@app.post("/coffee/", response_model=schemas.Coffee, tags=["coffee"])
async def post_coffee(coffee: schemas.CoffeeCreate, db: Session = Depends(get_db)):
    db_user = crud.get_coffee_by_name(db, coffee_name=coffee.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Coffee Already Exist!")
    return crud.create_coffee(db=db, coffee=coffee)


@app.put("/coffee/{coffee_name}", response_model=schemas.Coffee, tags=["coffee"])
async def put_coffee(coffee_name: str, db: Session = Depends(get_db),
                     sodium: float = 0.0, protein: float = 0.0,
                     dietary_fiber: float = 0.0,
                     sugars: float = 0.0,
                     saturated_fat: float = 0.0,
                     total_fat: float = 0.0,
                     total_carbohydrates: float = 0.0):
    return crud.update_coffee(coffee_name=coffee_name, db=db,
                              sodium=sodium, protein=protein,
                              dietary_fiber=dietary_fiber,
                              sugars=sugars,
                              saturated_fat=saturated_fat,
                              total_fat=total_fat,
                              total_carbohydrates=total_carbohydrates,
                              )
=======
>>>>>>> dev
