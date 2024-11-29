# myapp/tests/test_photo.py
from django.test import TestCase
from myapp.models import Photo, Album,User


class PhotoModelTest(TestCase):
    def setUp(self):
        """Test setup: Bir albüm ve fotoğraf oluşturuyoruz."""
        self.album = Album.objects.create(
            title="Holiday Pictures",
            user = User.objects.create(
            name="John Doe",
            username="johndoe",
            email="johndoe@example.com",
            phone="+1-800-555-5555",
            website="http://johndoe.com"
        )
        )
        self.photo = Photo.objects.create(
            title="Beach Sunset",
            album=self.album,
            url="http://example.com/photo.jpg",
            thumbnail_url="http://example.com/thumbnail.jpg"
        )

    def test_photo_creation(self):
        """Fotoğraf doğru şekilde oluşturulmalı."""
        photo = self.photo
        self.assertEqual(photo.title, "Beach Sunset")
        self.assertEqual(photo.album, self.album)
        self.assertEqual(photo.url, "http://example.com/photo.jpg")
        self.assertEqual(photo.thumbnail_url, "http://example.com/thumbnail.jpg")


    def test_photo_str_method(self):
        """Photo modelinin __str__ metodu doğru şekilde çalışmalı."""
        photo = self.photo
        self.assertEqual(str(photo), "Beach Sunset")
