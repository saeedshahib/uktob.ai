from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models import Author
from .models import Note


class NoteTestCase(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.author = Author.objects.create_user(username='saeed', password='saeedtest123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.author)

        # Create a sample note
        self.note = Note.objects.create(author=self.author, title="Sample Title", content="Sample Content")

    def test_create_note(self):
        """
        Ensure we can create a new note.
        """
        url = reverse('note-create')
        data = {'title': 'New Test Note 1', 'content': 'Test 1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 2)
        self.assertEqual(Note.objects.get(id=2).title, 'New Test Note 1')

    def test_read_note_detail(self):
        """
        Ensure we can read a single note detail.
        """
        url = reverse('note-detail', args=[self.note.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Sample Title')

    def test_update_note(self):
        """
        Ensure we can update an existing note.
        """
        url = reverse('note-detail', args=[self.note.id])
        data = {'title': 'Updated Note', 'content': 'Updated content'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_delete_note(self):
        """
        Ensure we can delete a note.
        """
        url = reverse('note-detail', args=[self.note.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 0)

    def tearDown(self):
        self.author.delete()
        self.note.delete()
