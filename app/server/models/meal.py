from pydantic import BaseModel, Field

class MealSchema(BaseModel):
    userid: str = Field(...)
    name: str = Field(...)
    calories: int = Field(...)

