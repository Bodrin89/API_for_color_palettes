#!/bin/bash -x

DJANGO_SETTINGS_MODULE=config.settings.prod python3 manage.py migrate --noinput || exit 1

DJANGO_SETTINGS_MODULE=config.settings.prod python3 manage.py collectstatic --noinput || exit 1

wait
exec "$@"
