from django.test import TestCase
from .models import Product, Category, Image


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a category for testing
        cls.category = Category.objects.create(name="Test Category")

        # Create a product for testing
        cls.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=100,
        )
        cls.product.category.add(cls.category)

    def test_product_string_representation(self):
        # Test the string representation of the product
        self.assertEqual(str(self.product), "Test Product")

    def test_product_category_association(self):
        # Check if the product is associated with the correct category
        self.assertEqual(self.product.category.first(), self.category)


class ImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a product for testing
        cls.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=100,
        )

    def test_image_creation(self):
        # Create an image associated with the product
        image = Image.objects.create(product=self.product, file="test_image.jpg")

        # Retrieve the image and check if it's associated with the correct product
        retrieved_image = Image.objects.get(id=image.id)
        self.assertEqual(retrieved_image.product, self.product)

    def test_image_string_representation(self):
        # Create an image associated with the product
        image = Image.objects.create(
            product=self.product, file="test_image.jpg", title="Test Title"
        )

        # Test the string representation of the image
        self.assertEqual(str(image), "Test Title")
