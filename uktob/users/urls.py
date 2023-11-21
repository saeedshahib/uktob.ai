from django.urls import path
from .views import AuthorRegistrationView, AuthorLoginView

urlpatterns = [
    path('register/', AuthorRegistrationView.as_view(), name='register'),
    path('login/', AuthorLoginView.as_view(), name='login'),
]
