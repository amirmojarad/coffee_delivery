from fastapi import FastAPI, Body
from app.model import Coffee

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


@app.get("/", tags=["root"])
async def get_root() -> dict:
    return {
        "message": "Welcome To Coffee Delivery"
    }


@app.get("/coffee_list", tags=["coffeeList"])
async def get_coffee_list() -> dict:
    return {
        "data": coffee_list
    }


@app.post("/coffee_list", tags=["coffeeList"])
async def add_coffee(coffee: Coffee = Body(...)) -> dict:
    coffee.id = len(coffee_list) + 1
    coffee_list.append(coffee)
    return {
        "status": "Coffee {} Added Successfully".format(coffee.name)
    }


@app.get("/coffee_list/{name}", tags=["coffeeList"])
async def get_coffee_by_name(name: str) -> dict:
    response = {}
    if len(coffee_list) == 0:
        response.update({"status": "list is empty"})
        return response
    for coffee in coffee_list:
        if coffee["name"] == name:
            response.update({
                "status": {
                    "data": [coffee]
                }
            }
            )
            return response
    response.update({"status": "Coffee with name {} not Found!".format(name)})
    return response
