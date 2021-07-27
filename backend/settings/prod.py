from .base import *

DEBUG = True
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('133.186.228.87', 6379)],
        }
    },
}
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