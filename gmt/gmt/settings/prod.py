import os
from gmt.settings.base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'PORT': os.environ.get("DB_PORT"),
        'HOST': os.environ.get("DB_HOST")
    }
}
