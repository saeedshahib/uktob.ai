from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response

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


class NoteSummarizeView(UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def put(self, request, *args, **kwargs):
        note = self.get_object()
        note.summarize_note_using_langchain()
        serializer = self.get_serializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)
