from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Address

User = get_user_model()


class AddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing
        cls.user = User.objects.create_user(
            username="test_user", password="test_password", phone="1234567890"
        )

    def test_address_creation(self):
        # Create an address associated with the user
        address = Address.objects.create(user=self.user, address="Test Address")

        # Retrieve the address and check if it's associated with the correct user
        retrieved_address = Address.objects.get(id=address.id)
        self.assertEqual(retrieved_address.user, self.user)

    def test_soft_delete(self):
        address = Address.objects.create(user=self.user, address="Test Address")

        # Soft delete the address
        address.delete()

        # Check if the address is logically deleted
        self.assertTrue(address.is_deleted)

    def test_deactivate_user(self):
        self.assertTrue(self.user.is_active)

        # Deactivate the user
        self.user.deactivate()

        # Check if the user is deactivated
        self.assertFalse(self.user.is_active)

    # def test_address_string_representation(self):
    #     address = Address.objects.create(user=self.user, address='Test Address')
    #     self.assertEqual(str(address), 'Test Address')


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing
        cls.user = User.objects.create_user(
            username="test_user",
            password="test_password",
            phone="1234567890",
            first_name="John",
            last_name="Doe",
        )

    def test_user_string_representation(self):
        # Test the string representation of the user
        self.assertEqual(str(self.user), "John Doe")

    def test_user_deactivate(self):
        # Ensure the user is initially active
        self.assertTrue(self.user.is_active)

        # Deactivate the user
        self.user.deactivate()

        # Check if the user is deactivated
        self.assertFalse(self.user.is_active)

    def test_user_activate(self):
        # Deactivate the user first
        self.user.deactivate()

        # Ensure the user is initially inactive
        self.assertFalse(self.user.is_active)

        # Activate the user
        self.user.activate()

        # Check if the user is activated
        self.assertTrue(self.user.is_active)
