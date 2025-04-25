from fastapi import FastAPI, Depends, HTTPException,status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models import User, Token, UserCreate
from auth import (
    fake_users_db,
    authenticate_user,
    create_access_token,
    get_current_active_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    get_password_hash,
)
from datetime import timedelta
from middleware import log_middleware
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

# Add middleware
app.middleware("http")(log_middleware)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#routes

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get("/users/me/items")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

@app.get("/users", response_model=list[User])
async def get_all_users(current_user: User = Depends(get_current_active_user)):
    # Only return basic user info (without passwords)
    users = []
    for username, user_data in fake_users_db.items():
        users.append(User(**{k: v for k, v in user_data.items() if k != "hashed_password"}))
    return users

@app.post("/users", response_model=User)
async def create_user(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    user_data = {
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": hashed_password,
        "disabled": False,
    }
    fake_users_db[user.username] = user_data
    return User(**{k: v for k, v in user_data.items() if k != "hashed_password"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)