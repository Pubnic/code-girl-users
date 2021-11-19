from typing import List
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from database import UserDatabase
from serializers import CreateUserSerializer, UserSerializer

app = FastAPI()
user_database = UserDatabase()

@app.get('/status/')
def status_ok():
    return {"status": "ok"}

'''
    CRUD = Create, Read, Update, Delete
'''
# CREATE USER
@app.post(
    '/users/',
    status_code=status.HTTP_201_CREATED,
    response_model=UserSerializer
)
def create_user(user: CreateUserSerializer):
    new_user = user_database.add_user(user.dict())
    return new_user

# GET USERS
@app.get('/users/', response_model=List[UserSerializer])
def get_users():
    return user_database.get_users()

# GET USER BY ID
@app.get('/users/{user_id}/', response_model=UserSerializer)
def get_user(user_id: str):
    user = user_database.get_user(user_id)
    if user is None:
        return JSONResponse(
            content={'message': 'User not found'},
            status_code=status.HTTP_404_NOT_FOUND
        )
    return user

# UPDATE USER BY ID
# @app.put('/users/{user_id}/')
# def update_user(user_id: str, user: CreateUserSerializer):

# DELETE USER BY ID
@app.delete('/users/{user_id}/')
def delete_user(user_id: str, status_code=status.HTTP_204_NO_CONTENT):
    deleted = user_database.delete_user(user_id)
    if not deleted:
        return JSONResponse(
            content={'message': 'User not found'},
            status_code=status.HTTP_404_NOT_FOUND
        )