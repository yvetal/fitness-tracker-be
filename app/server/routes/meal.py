from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

import server.crud.meal as crud  
from server.models.meal import MealSchema

router = APIRouter()

@router.post("/", response_description="Meal added")
async def add_data(data: MealSchema = Body(...)):
    data = jsonable_encoder(data)
    new_item = await crud.add(data)
    return ResponseModel(new_item, "Meal added successfully.")

@router.get("/", response_description="Meals retrieved")
async def get_for_user(userid: str):    
    items = await crud.retrieve_for_user(userid)
    if items:
        return ResponseModel(items, "Meal data retrieved successfully")
    return ResponseModel(items, "Empty list returned")

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}