# myapp/tests/test_company.py
from django.test import TestCase
from myapp.models import Company, User


class CompanyModelTest(TestCase):
    def setUp(self):
        """Test setup: Bir kullanıcı ve company oluşturuyoruz."""
        self.user = User.objects.create(
            name="John Doe",
            username="johndoe",
            email="johndoe@example.com",
            phone="+1-800-555-5555",
            website="http://johndoe.com"
        )
        self.company = Company.objects.create(
            name="Tech Corp",
            catch_phrase="Innovating the future",
            bs="Tech solutions",
            user=self.user
        )

    def test_company_creation(self):
        """Company doğru şekilde oluşturulmalı."""
        company = self.company
        self.assertEqual(company.name, "Tech Corp")
        self.assertEqual(company.catch_phrase, "Innovating the future")
        self.assertEqual(company.bs, "Tech solutions")
        self.assertEqual(company.user, self.user)

    def test_company_str_method(self):
        """Company modelinin __str__ metodu doğru şekilde çalışmalı."""
        company = self.company
        self.assertEqual(str(company), "Tech Corp")
