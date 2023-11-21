from django.shortcuts import render

# Create your views here.

from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Author
from .serializers import AuthorSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class AuthorRegistrationView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorLoginView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
