from fastapi import FastAPI

from server.routes.activity_log import router as ActivityLogRouter
from server.routes.goal import router as GoalRouter
from server.routes.user import router as UserRouter
from server.routes.devices import router as DeviceRouter
from server.routes.meal import router as MealRouter
from server.routes.workout_plan import router as WorkoutPlanRouter

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(ActivityLogRouter, tags=["ActivityLog"], prefix="/activity-logs")
app.include_router(GoalRouter, tags=["Goal"], prefix="/goals")
app.include_router(UserRouter, tags=["User"], prefix="/users")
app.include_router(DeviceRouter, tags=["Device"], prefix="/devices")
app.include_router(MealRouter, tags=["Meal"], prefix="/meals")
app.include_router(WorkoutPlanRouter, tags=["WorkoutPlan"], prefix="/workout-plans")


@app.get("/", tags=["Root"])
async def read_root():
    
    return {"message": "Welcome to this fantastic app!"}