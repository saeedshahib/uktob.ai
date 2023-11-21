from rest_framework import serializers
from .models import Note
from users.serializers import AuthorSerializer


class NoteSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)

    class Meta:
        model = Note
        fields = ['id', 'author', 'title', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']
