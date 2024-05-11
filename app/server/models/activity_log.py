from pydantic import BaseModel, Field

class ActivityLogSchema(BaseModel):
    type: str = Field(...)
    distance: int = Field(...)
    calories: int = Field(...)
    intensity: int = Field(...)
    duration: int = Field(...)

