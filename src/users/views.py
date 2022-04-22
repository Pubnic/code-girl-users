from fastapi import APIRouter
from fastapi.responses import JSONResponse
from users.services import UserService
from users.serializers import AddressSerializer, UserSerializer


users_router = APIRouter()


@users_router.get(
    '/last_user/',
    response_model=UserSerializer
)
def get_last_user():
    try:
        user_service = UserService()
        user, addresses = user_service.get_last_user()

        addresses_serializer: list[AddressSerializer] = []
        for address in addresses:
            address_serializer = AddressSerializer(
                address=address.address,
                city=address.city,
                state=address.state,
                zip_code=address.zip_code,
            )
            addresses_serializer.append(address_serializer)

        user_serializer = UserSerializer(
            username=user.username,
            email=user.email,
            addresses=addresses_serializer
        )
        return user_serializer
    except Exception:
        return JSONResponse(status_code=404, content={"message": "User not found"})
