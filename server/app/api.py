from fastapi import FastAPI, Body, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import status

from app.model import Coffee, User

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
        "name": "coffeeList",
        "description": "Manage coffees",
    },
    {
        "name": "purchase",
        "description": "Purchase Coffee, Involve User and Coffee list"
    }
]

app = FastAPI(title="Coffee Delivery Project", description="Purchase, Show Coffee List, etc!", version="0.1.0",
              tags_metadata=tags_metadata)

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

coffee_list = [
    {
        "id": 1,
        "name": "Americano",
        "caffeine": 255.0,
        "ingredients": ["Water", "Brewed Espresso"]
    },
    {
        "id": 3,
        "name": "temp",
        "caffeine": 255.0,
        "ingredients": ["Water", "Brewed Espresso"]
    },
    {
        "id": 4,
        "name": "liam",
        "caffeine": 255.0,
        "ingredients": ["Water", "Brewed Espresso"]
    }
]


def fake_hash_password(password: str):
    return "fakehashed" + password


# def hash_password(password: str):
#     salt = uuid.uuid4().hex
#     hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
#     return hashed_password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")





def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(coffee_list, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get("/", tags=["root"])
async def get_root() -> dict:
    return {
        "message": "Welcome To Coffee Delivery"
    }


@app.get("/coffee_list/all", tags=["coffeeList"])
async def get_coffee_list() -> dict:
    return {
        "data": coffee_list
    }


@app.post("/coffee_list", tags=["coffeeList"])
async def add_coffee(coffee: Coffee = Body(...)) -> dict:
    coffee.id = len(coffee_list) + 1
    coffee_list.append(coffee.dict())
    return {
        "status": "Coffee {} Added Successfully".format(coffee.name)
    }


@app.get("/coffee_list/{name}", tags=["coffeeList"])
async def get_coffee_by_name(name: str) -> dict:
    response = {}
    if len(coffee_list) == 0:
        raise HTTPException(status_code=200, detail="Coffee List is Empty")
    for coffee in coffee_list:
        if coffee["name"] == name:
            response.update({
                "status": {
                    "data": [coffee]
                }
            }
            )
            return response
    raise HTTPException(status_code=404, detail="Coffee with name {} not Found!".format(name))
