from rest_framework import serializers
from .models import Board, BoardMedia, BoardComment


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'


class BoardMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardMedia
        fields = '__all__'


class BoardCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardComment
        fields = '__all__'