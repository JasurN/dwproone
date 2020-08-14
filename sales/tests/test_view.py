from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from sales.models import Box, Customer
from sales.tests.sales_test_utilites import create_number_model_instance, create_user
from sales.views import CustomerListView


class CustomerListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_number_model_instance(Customer, number_customers=10, name='Customer')
        create_user()

    def test_customer_list_view_authentication(self):
        response = self.client.get('/api/sales/customer/all/')
        self.assertEqual(response.status_code, 401)

    def test_customer_list_view_exists_at_desired_local(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/sales/customer/all/')
        view = CustomerListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)


class BoxListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_number_model_instance(Customer, number_customers=10, name='Customer')
        create_user()

    def test_box_list_view_authentication(self):
        response = self.client.get('/api/sales/box/all/')
        self.assertEqual(response.status_code, 401)

    def test_something(self):
        pass
