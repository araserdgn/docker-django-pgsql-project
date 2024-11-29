# myapp/tests/test_post.py

from django.test import TestCase
from myapp.models import Post, User


class PostModelTest(TestCase):
    def setUp(self):
        """Test setup: Bir kullanıcı ve post oluşturuyoruz."""
        self.user = User.objects.create(
            name="John Doe",
            username="johndoe",
            email="johndoe@example.com",
            phone="+1-800-555-5555",
            website="http://johndoe.com"
        )
        self.post = Post.objects.create(
            title="First Post",
            body="This is the body of the first post.",
            user=self.user
        )

    def test_post_creation(self):
        """Post doğru şekilde oluşturulmalı."""
        post = self.post
        self.assertEqual(post.title, "First Post")
        self.assertEqual(post.body, "This is the body of the first post.")
        self.assertEqual(post.user, self.user)

    def test_post_str_method(self):
        """Post modelinin __str__ metodu doğru şekilde çalışmalı."""
        post = self.post
        self.assertEqual(str(post), "First Post")
