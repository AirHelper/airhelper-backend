from rest_framework import serializers
from .models import Room, GameType, AttendedUser
from cert.serializers import CustomUserSerializer


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class AttendedUserSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = AttendedUser
        fields = '__all__'