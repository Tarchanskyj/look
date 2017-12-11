from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from product.models import Product


class UrlsTest(TestCase):

    def test_view_url_exists_main(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_exists_products(self):
        resp = self.client.get(reverse('product:products_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_exists_login(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

