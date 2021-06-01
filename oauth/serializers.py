from collections import OrderedDict
from rest_framework import serializers

from cert.models import CustomUser
from .models import SocialUser


class SocialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialUser
        fields = '__all__'


class OauthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['call_sign', 'is_active']
        extra_kwargs = {
            'call_sign': {'allow_null': False, 'required': True},
        }
