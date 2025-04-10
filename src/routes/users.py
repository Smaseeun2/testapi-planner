from fastapi import APIRouter, HTTPException, status

from src.models.users import UserSignIn

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

users = {}
"""
users = {
    "unerue@me.com" :
    "email" :
    "password" : "1234",
    "events" : None}
    }    
"""

@user_router.post("/signup")
async def sign_new_user(user: str):
    """회원가입"""
    if user in users:
        raise HTTPException(
            status_code=status.HTTP_400_CONfLICT,
            detail="User already exists")
    users[user.email] = user
    return {"meassage" : "User successfully created"}

@user_router.post("/signin")
async def sign_user_in(credentials: UserSignIn):
    """회원가입이 끝난 회원 로그인하는 API"""
    if credentials.email not in users:
        raise HTTPEXeption(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    stored_user = users[credentials.email]
    if stored_user.password != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Incorrect password"
        )
    return {"message": "User successfully signed in"}
