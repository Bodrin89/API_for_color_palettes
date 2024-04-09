# tasks.py
from time import sleep

import requests
from celery import shared_task

from apps.color.dao import ColorDAO
from config.settings.base import URL_GET_COLOR_NAME


@shared_task
def fetch_and_save_color_name(hex_value, obj_id):
    """Celery задача для получения и сохранения имени цвета."""

    url = URL_GET_COLOR_NAME
    sleep(5)
    response = requests.get(url=url, params={'hex': hex_value})
    if response.status_code != 200:
        raise Exception(f'Ошибка при получении данных цвета: {response.status_code}')

    color_name = response.json()['name']['value']
    color = ColorDAO.get_color_by_id(obj_id)
    color.name = color_name
    color.save()
