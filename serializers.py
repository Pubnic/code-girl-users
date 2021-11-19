from pydantic import BaseModel
from typing import Optional


class CreateUserSerializer(BaseModel):
    username: str
    name: str
    birth_date: Optional[str]


class UserSerializer(CreateUserSerializer):
    id: str
