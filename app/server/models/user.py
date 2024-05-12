from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    userid: str = Field(...)
    password: str = Field(...)


class LoginSchema(BaseModel):
    userid: str = Field(...)
    password: str = Field(...)