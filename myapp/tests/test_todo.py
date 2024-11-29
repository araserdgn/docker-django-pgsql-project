# myapp/tests/test_todo.py
from django.test import TestCase
from myapp.models import Todo, User


class TodoModelTest(TestCase):
    def setUp(self):
        """Test setup: Bir kullanıcı ve todo oluşturuyoruz."""
        self.user = User.objects.create(
            name="John Doe",
            username="johndoe",
            email="johndoe@example.com",
            phone="+1-800-555-5555",
            website="http://johndoe.com"
        )
        self.todo = Todo.objects.create(
            title="Buy Groceries",
            user=self.user,
            completed=False
        )

    def test_todo_creation(self):
        """Todo doğru şekilde oluşturulmalı."""
        todo = self.todo
        self.assertEqual(todo.title, "Buy Groceries")
        self.assertEqual(todo.user, self.user)
        self.assertFalse(todo.completed)

    def test_todo_str_method(self):
        """Todo modelinin __str__ metodu doğru şekilde çalışmalı."""
        todo = self.todo
        self.assertEqual(str(todo), "Buy Groceries")
