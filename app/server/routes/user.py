from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

import server.crud.user as crud  
from server.models.user import UserSchema, LoginSchema

router = APIRouter()

@router.post("/login", response_description="Logged in")
async def add_data(data: LoginSchema = Body(...)):
    data = jsonable_encoder(data)
    retrieved_user = await crud.retrieve(data['userid'])
    if not retrieved_user:
        login_status = 'Failure'
        return ErrorResponseModel(login_status, 401, 'User authentication failed')
    
    if retrieved_user['password'] == data['password']:
        login_status = 'Success'
        return ResponseModel(login_status, "User login verified.")
    else:
        login_status = 'Failure'
        return ErrorResponseModel(login_status, 401, 'User authentication failed')

@router.post("/", response_description="Added user")
async def add_data(data: UserSchema = Body(...)):
    data = jsonable_encoder(data)
    if await crud.retrieve(data['userid']):
        return ErrorResponseModel('User already exists', 400, 'User already exists')
    new_item = await crud.add(data)
    return ResponseModel(new_item, "User added successfully.")

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}