from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

import server.crud.devices as crud  
from server.models.devices import WearableDeviceSchema

router = APIRouter()

@router.post("/", response_description="Device added")
async def add_data(data: WearableDeviceSchema = Body(...)):
    try:
        data = jsonable_encoder(data)
        new_item = await crud.add(data)
        return ResponseModel(new_item, "Device added successfully.")
    except:
        return ErrorResponseModel('Failed to add device', 400, 'Failed to add device')\
        
@router.get("/", response_description="Devices retrieved")
async def get_for_user(userid: str):
    item = await crud.retrieve_for_user(userid)
    if item:
        item['deviceId'] =  item['_id']
        return ResponseModel(item, "Device data retrieved successfully")
    else:
        return ResponseModel({}, "Empty list returned")

@router.delete("/", response_description="Devices deleted")
async def get_for_user(userid: str):
    try:
        item = await crud.delete_for_user(userid)
        return ResponseModel({}, "Device data retrieved successfully")
    except:
        return ErrorResponseModel("Could not delete!", 400, "Could not delete!")

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}