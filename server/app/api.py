from fastapi import FastAPI

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


@app.get("/", tags=["root"])
async def get_root() -> dict:
    return {
        "message": "Welcome To Coffee Delivery"
    }


