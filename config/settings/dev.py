from datetime import timedelta

from config.settings.base import *  # noqa

THIRD_PARTY_APPS += [  # noqa
    'debug_toolbar',
]


MIDDLEWARE += [  # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS  # noqa

DEBUG = True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=4000),
}
