from fastapi import HTTPException, Depends
from app import schemas
from app.auth import auth


async def get_current_active_user(current_user: schemas.User = Depends(auth.get_current_user)):
    if current_user.is_active:
        return current_user
    raise HTTPException(status_code=400, detail="Inactive user")

# async def sign_up_user()
