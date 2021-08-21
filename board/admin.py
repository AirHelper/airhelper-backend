from django.contrib import admin
from .models import Board, BoardMedia, BoardComment

# Register your models here.
admin.site.register(Board)
admin.site.register(BoardMedia)
admin.site.register(BoardComment)