from django.test import TestCase
from product.forms import CommentModelForm, LikeModelForm
from product.models import Product, Comment, Like


class FormsTest(TestCase):

    def comment_test_valid_form(self):
        comment = Comment.objects.create(text='Comment text', author='user')
        data = {'text': comment.text, 'author': comment.author}
        form = CommentModelForm(data=data)
        self.assertFalse(form.is_invalid())

    def like_test_valid_form(self):
        product = Product.objects.create(name='test name', slug='test-name', description='adminadmin', price='23')
        user = User.objects.create_user('admin', 'admin@gmail.com', 'adminadmin')
        like = Like.objects.create_user(product=product, user=user)
        data = {'text': like.user, 'product': like.product}
        form = LikeModelForm(data=data)
        self.assertFalse(form.is_invalid())


# Create your tests here.
