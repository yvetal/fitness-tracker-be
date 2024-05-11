from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

import server.crud.goal as crud  
from server.models.goal import GoalSchema

router = APIRouter()

@router.post("/", response_description="Goal added")
async def add_data(data: GoalSchema = Body(...)):
    data = jsonable_encoder(data)
    new_item = await crud.add(data)
    return ResponseModel(new_item, "Goal added successfully.")

@router.get("/", response_description="Goals retrieved")
async def get_all():    
    items = await crud.retrieve_all()
    if items:
        return ResponseModel(items, "Goal data retrieved successfully")
    return ResponseModel(items, "Empty list returned")

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}