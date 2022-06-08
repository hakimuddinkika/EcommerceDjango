from http import client
from turtle import title
from unicodedata import category
from urllib import response
from django.http import HttpRequest
from django.test import Client, TestCase

from unittest import skip


from django.contrib.auth.models import User
from django.urls import reverse
from store.models import Category, Product


# @skip('demonstrating skipping')
# class TestSkip(TestCase):

#     def test_skip_example(self):
#         pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                slug='django-beginners', price='20.00', image='django')

    def test_url_allowed_hosts(self):
        """
        Test Allowed Hosts
        """
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product response status
        """
        response = self.c.get(reverse('store:product_detail',args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category response status
        """
        response = self.c.get(reverse('store:category_list',args=['django']))
        self.assertEqual(response.status_code, 200)

    # def test_homepage_html(self):
    #     """
    #     Example: code validation, search HTML for text
    #     """
    #     request = HttpRequest()
    #     response = all_products(request)
    #     html = response.context.decode('utf8')
    #     self.assertIn('<title>BookStore</title>', html)
    #     self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
    #     self.assertEqual(response.status_code, 200)

    # def test_view_function(self):
    #     """
    #     Example: Using request Factory
    #     """
    #     request = self.factory.get('/django-beginners')
    #     response = all_products(request)
    #     html = response.context.decode('utf8')
    #     self.assertIn('<title>BookStore</title>', html)
    #     self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
    #     self.assertEqual(response.status_code, 200)