from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Note
from .serializers import NoteSerializer


class NoteView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
