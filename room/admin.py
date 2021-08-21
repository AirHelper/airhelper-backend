from django.contrib import admin
from .models import Room, AttendedUser, GameType

# Register your models here.
admin.site.register(Room)
admin.site.register(AttendedUser)
admin.site.register(GameType)