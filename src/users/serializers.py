from pydantic import BaseModel


class AddressSerializer(BaseModel):
    address: str
    city: str
    state: str
    zip_code: str


class UserSerializer(BaseModel):
    username: str
    email: str
    addresses: list[AddressSerializer]
