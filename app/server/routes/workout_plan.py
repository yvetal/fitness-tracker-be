from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

import server.crud.workout_plan as crud  
from server.models.workout_plan import WorkoutPlanSchema

router = APIRouter()


@router.get("/", response_description="Workout Plans retrieved")
async def get(difficulty):    
    items = await crud.retrieve_by_difficulty(difficulty)
    if items:
        return ResponseModel(items, "WorkoutPlan data retrieved successfully")
    return ResponseModel(items, "Empty list returned")

@router.post("/add-dummies", response_description="Dummy Workout Plans added")
async def add_dummies():    
    await crud.add_dummies()
    return ResponseModel('Dummy data added', 'Dummy data added')


@router.post("/", response_description="Workout Plan added")
async def add(data: WorkoutPlanSchema):    
    data = jsonable_encoder(data)
    added_data = await crud.add(data)
    return ResponseModel(added_data, 'Workout plan added')

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}