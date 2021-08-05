from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..database import Base
from ..api import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


# Coffee Section Test

def test_get_coffee():
    response = client.get("/coffee/")
    assert response.status_code == 200
    assert len(response.json()) == 7


def test_get_coffee_image():
    coffee_name = "Americano"
    response = client.get(f"/coffee/{coffee_name}/image/", )
    assert response.status_code == 200


# User Section Test
def test_user_sign_up():
    username = "test2"
    response = client.post("/users/sign_up", data={"username": username, "password": "test_password"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] is None
    assert data["username"] == username
    assert len(data["access_token"]) == 124


def test_get_user():
    username = "new_test"
    make_user_response = client.post("/users/sign_up", data={"username": username, "password": "test_password"})
    assert make_user_response.status_code == 200
    access_token = make_user_response.json()["access_token"]
    response = client.get(f"/users/{username}", headers={"token": access_token})
    assert response.status_code == 200


def test_put_user():
    username = "new_test2"
    full_name = "full_name"
    email = "email"
    make_user_response = client.post("/users/sign_up", data={"username": username, "password": "test_password"})
    assert make_user_response.status_code == 200
    access_token = make_user_response.json()["access_token"]
    response = client.put(f"/users/{username}", headers={"token": access_token},
                          params={"full_name": full_name, "email": email})
    assert response.status_code == 200
    data = response.json()
    assert data["full_name"] == full_name
    assert data["email"] == email


def test_post_coffee_to_user():
    username = "new_test6"
    sign_up_response = client.post("/users/sign_up", data={"username": username, "password": "32"})
    assert sign_up_response.status_code == 200
    access_token = sign_up_response.json()["access_token"]
    coffee_name = "Americano"
    response = client.post(f"/users/{username}/coffee/", params={"coffee_name": coffee_name},
                           headers={"token": access_token})
    assert response.status_code == 200
