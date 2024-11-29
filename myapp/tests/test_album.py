# myapp/tests/test_album.py
from django.test import TestCase
from myapp.models import Album, User


class AlbumModelTest(TestCase):
    def setUp(self):
        """Test setup: Bir kullanıcı ve albüm oluşturuyoruz."""
        self.user = User.objects.create(
            name="John Doe",
            username="johndoe",
            email="johndoe@example.com",
            phone="+1-800-555-5555",
            website="http://johndoe.com"
        )
        self.album = Album.objects.create(
            title="Holiday Pictures",
            user=self.user
        )

    def test_album_creation(self):
        """Albüm doğru şekilde oluşturulmalı."""
        album = self.album
        self.assertEqual(album.title, "Holiday Pictures")
        self.assertEqual(album.user, self.user)

    def test_album_str_method(self):
        """Album modelinin __str__ metodu doğru şekilde çalışmalı."""
        album = self.album
        self.assertEqual(str(album), "Holiday Pictures")
