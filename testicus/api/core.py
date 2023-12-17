import base64

from rest_framework import serializers
from django.core.files.base import ContentFile


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


def get_percent(a, b):
    if a != 0:
        return int(a / b * 100)
    raise ZeroDivisionError()


def get_object_id_from_url(path, text_before, text_after):
    str_path = str(path)
    start_index_id = str_path.find(text_before) + len(text_before)
    end_index_id = str_path.find(text_after)
    object_id = int(str_path[start_index_id:end_index_id])
    return object_id
