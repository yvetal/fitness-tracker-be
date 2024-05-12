from pydantic import BaseModel, Field

class GoalSchema(BaseModel):
    currentActivityLevel: str = Field(...)
    currentWeight: int = Field(...)
    currentHeight: int = Field(...)
    goal: int = Field(...)
    difficulty: str = Field(...)
    userid: str = Field(...)

