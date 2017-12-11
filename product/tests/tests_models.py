from django.test import TestCase
from product.models import Product, Comment, Like


class ModelsTest(TestCase):

    def test_model_product(self):
        Product.objects.create(name='test name', slug='test-name', description='adminadmin', price='23')
        self.assertEqual(Product.objects.all().count(), 1)

    def test_model_comment(self):
        product = Product.objects.create(name='test name', slug='test-name', description='adminadmin', price='23')
        Comment.objects.create(product=product, author='test', text='adminadmin')
        self.assertEqual(Comment.objects.all().count(), 1)

    def test_model_like_without_user(self):
        product = Product.objects.create(name='test name', slug='test-name', description='adminadmin', price='23')
        Like.objects.create(product=product)
        self.assertEqual(Like.objects.all().count(), 1)
