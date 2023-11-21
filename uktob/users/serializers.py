from rest_framework import serializers
from .models import Author
from django.contrib.auth.hashers import make_password


class AuthorSerializer(serializers.ModelSerializer):
    cell_phone = serializers.CharField(required=False)

    class Meta:
        model = Author
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'cell_phone']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(self.context['request'].data)
        validated_data['password'] = make_password(validated_data['password'])
        instance: Author = super().create(validated_data)
        return instance
