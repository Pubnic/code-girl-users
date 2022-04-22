from users.models import AddressModel, UserModel


class UserService:
    def get_last_user(self):
        user: UserModel = UserModel.objects.last()

        if not user:
            raise Exception('User not found')
        else:
            addresses: list[AddressModel] = user.addresses.all()
            return user, addresses
