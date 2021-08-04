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




