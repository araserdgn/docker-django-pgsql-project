# myapp/tests/test_user.py
from django.test import TestCase
from myapp.models import User


class UserModelTest(TestCase):
    def setUp(self):
        """Test setup: Bir kullanıcı oluşturuyoruz."""
        self.user = User.objects.create(
            name="John Doe",
            username="johndoe",
            email="johndoe@example.com",
            phone="+1-800-555-5555",
            website="http://johndoe.com"
        )

    def test_user_creation(self):
        """Kullanıcı doğru şekilde oluşturulmalı."""
        user = self.user
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.username, "johndoe")
        self.assertEqual(user.email, "johndoe@example.com")
        self.assertEqual(user.phone, "+1-800-555-5555")
        self.assertEqual(user.website, "http://johndoe.com")

    def test_user_str_method(self):
        """User modelinin __str__ metodu doğru şekilde çalışmalı."""
        user = self.user
        self.assertEqual(str(user), "John Doe")
