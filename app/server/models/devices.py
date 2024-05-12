from pydantic import BaseModel, Field

class WearableDeviceSchema(BaseModel):
    name: str = Field(...)
    userid: str = Field(...)


