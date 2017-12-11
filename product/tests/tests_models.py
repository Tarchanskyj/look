from django.test import TestCase
from django.contrib.auth.models import User
from product.models import Product, Comment, Like


class ModelsTest(TestCase):

    def test_model_product(self):
        product = Product.objects.create(name='test name', slug='test-name', description='adminadmin', price='23')
        self.assertEqual(Product.objects.all().count(), 1)
        self.assertEqual(product.__str__(), product.name)

    def test_model_comment(self):
        product = Product.objects.create(name='test name', slug='test-name', description='adminadmin', price='23')
        comment = Comment.objects.create(product=product, author='test', text='adminadmin')
        self.assertEqual(Comment.objects.all().count(), 1)
        self.assertEqual(comment.__str__(), comment.author + ' - ' + comment.product.name)

    def test_model_like(self):
        product = Product.objects.create(name='test name', slug='test-name', description='adminadmin', price='23')
        user = User.objects.create_user('admin', 'admin@gmail.com', 'adminadmin')
        like = Like.objects.create(product=product, user=user)
        self.assertEqual(Like.objects.all().count(), 1)
        self.assertEqual(like.__str__(), like.user.username + ' - ' + like.product.name)
