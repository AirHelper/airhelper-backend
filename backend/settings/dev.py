
"""
Django settings for backend project.
Generated by 'django-admin startproject' using Django 3.1.3.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from .base import *
import os
import json

DEBUG = True
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases'
SYSTEM_ENV = os.environ.get('SYSTEM_ENV', None)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('172.23.0.1', 6379)],
        }
    },
}

if SYSTEM_ENV is None:
    print('로컬 개발용')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'airhelperdev',
            'USER': 'airhelper',
            'PASSWORD': 'airhelper',
            'HOST': 'psqldb',
            'PORT': 5432,
        }
    }
else:
    print('깃허브 액션 테스트용')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'airhelperdev',
            'USER': 'airhelper',
            'PASSWORD': 'airhelper',
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }
