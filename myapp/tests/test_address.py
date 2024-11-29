# myapp/tests/test_address.py
from django.test import TestCase
from myapp.models import Address, User


class AddressModelTest(TestCase):
    def setUp(self):
        """Test setup: Bir kullanıcı ve adres oluşturuyoruz."""
        self.user = User.objects.create(
            name="John Doe",
            username="johndoe",
            email="johndoe@example.com",
            phone="+1-800-555-5555",
            website="http://johndoe.com"
        )
        self.address = Address.objects.create(
            street="123 Main St",
            suite="Suite 500",
            city="Springfield",
            zipcode="12345",
            geo_lat="40.712776",
            geo_lng="-74.005974",
            user=self.user
        )

    def test_address_creation(self):
        """Address doğru şekilde oluşturulmalı."""
        address = self.address
        self.assertEqual(address.street, "123 Main St")
        self.assertEqual(address.suite, "Suite 500")
        self.assertEqual(address.city, "Springfield")
        self.assertEqual(address.zipcode, "12345")
        self.assertEqual(address.geo_lat, "40.712776")
        self.assertEqual(address.geo_lng, "-74.005974")
        self.assertEqual(address.user, self.user)

    def test_address_str_method(self):
        """Address modelinin __str__ metodu doğru şekilde çalışmalı."""
        address = self.address
        self.assertEqual(str(address), "123 Main St, Springfield")
