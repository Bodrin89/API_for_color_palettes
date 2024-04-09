from pytest_factoryboy import register

from tests.factories import ColorFactory, PaletteFactory, UserFactory

pytest_plugins = 'tests.fixtures'

register(UserFactory)
register(PaletteFactory)
register(ColorFactory)
