import factory
from factory.django import DjangoModelFactory

from apps.color.models import ColorModel
from apps.palette.models import PaletteModel
from apps.user.models import UserModel


class UserFactory(DjangoModelFactory):
    class Meta:
        model = UserModel

    username = factory.Faker('user_name')
    password = factory.Faker('password')
    login = factory.Faker('user_name')


class PaletteFactory(DjangoModelFactory):
    class Meta:
        model = PaletteModel

    name = factory.Faker('word')
    user = factory.SubFactory(UserFactory)


class ColorFactory(DjangoModelFactory):
    class Meta:
        model = ColorModel

    name = factory.Faker('word')
    hex = factory.Faker('hex_color')
    palette = factory.SubFactory(PaletteFactory)
