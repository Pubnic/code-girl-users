from django.db import models
from pydantic import EmailStr
from common.models import BaseModel


class UserModel(BaseModel):
    username: str = models.CharField(max_length=50, unique=True)
    email: EmailStr = models.EmailField(unique=True)


class AddressModel(BaseModel):
    address: str = models.CharField(max_length=50)
    city: str = models.CharField(max_length=50)
    state: str = models.CharField(max_length=50)
    zip_code: str = models.CharField(max_length=50)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='addresses')
