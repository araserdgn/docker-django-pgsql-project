# myapp/tests/test_comment.py

from django.test import TestCase
from myapp.models import Comment, User, Post


class CommentModelTest(TestCase):
    def setUp(self):
        """Test setup: Bir kullanıcı, post ve yorum oluşturuyoruz."""
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
        self.comment = Comment.objects.create(
            body="This is a comment.",
            email="johndoe@example.com",
            name="John Doe",
            post=self.post
        )

    def test_comment_creation(self):
        """Yorum doğru şekilde oluşturulmalı."""
        comment = self.comment
        self.assertEqual(comment.body, "This is a comment.")
        self.assertEqual(comment.email, "johndoe@example.com")
        self.assertEqual(comment.name, "John Doe")
        self.assertEqual(comment.post, self.post)

    def test_comment_str_method(self):
        """Comment modelinin __str__ metodu doğru şekilde çalışmalı."""
        comment = self.comment
        self.assertEqual(str(comment), f"Comment by {self.user.name} on {self.post.title}")  # Testi uyarlıyoruz