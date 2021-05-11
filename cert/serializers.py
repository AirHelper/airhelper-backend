import collections
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)

        if 'password' in validated_data:  # patch password
            user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        exclude = ['is_admin', 'is_staff']
        extra_kwargs = {"password": {"write_only": True}}


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = CustomUser(
            user_id=validated_data['user_id'],
            email=validated_data['email'],
            name=validated_data['name'],
            call_sign=validated_data['call_sign']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ("id", "user_id", "password", "name", "call_sign", "email")
        extra_kwargs = {"password": {"write_only": True}}
