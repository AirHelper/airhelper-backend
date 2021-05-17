from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'airhelper-db',
        'USER': 'airhelperdev',
        'PASSWORD': 'airhelperdev',
        'HOST': '133.186.244.147',
        'PORT': 5432,
    }
}