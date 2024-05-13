from pydantic import BaseModel, Field

class WorkoutPlanElementSchema(BaseModel):
    type: str = Field(...)
    distance: int = Field(...)

class WorkoutPlanSchema(BaseModel):
    name: str = Field(...)
    difficulty: str = Field(...)
    elements: list[WorkoutPlanElementSchema] = Field(...)
