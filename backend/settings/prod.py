from .base import *
print('배포용')
DEBUG = True
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis_service', 6379)],
        }
    },
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'airhelper-db',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': '146.56.157.132',
        'PORT': 5432,
    }
}
