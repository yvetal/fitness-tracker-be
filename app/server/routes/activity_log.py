from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

import server.crud.activity_log as crud  
from server.models.activity_log import ActivityLogSchema

router = APIRouter()

@router.post("/", response_description="Activity Log added")
async def add_data(data: ActivityLogSchema = Body(...)):
    data = jsonable_encoder(data)
    new_item = await crud.add(data)
    return ResponseModel(new_item, "Activity Log added successfully.")

@router.get("/", response_description="Activity Logs retrieved")
async def get_for_user(userid: str):    
    items = await crud.retrieve_for_user(userid)
    if items:
        return ResponseModel(items, "Activity Log data retrieved successfully")
    return ResponseModel(items, "Empty list returned")

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}