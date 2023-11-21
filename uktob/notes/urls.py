from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteView, NoteSummarizeView

urlpatterns = [
    path('', NoteView.as_view(), name='note-create'),
    path('<int:pk>/', NoteView.as_view(), name='note-detail'),
    path('summarize/<int:pk>/', NoteSummarizeView.as_view(), name='summarize-note')
]
