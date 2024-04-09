from apps.user.models import UserModel


class UserDAO:
    @staticmethod
    def create_user(data):
        return UserModel.objects.create_user(**data)
