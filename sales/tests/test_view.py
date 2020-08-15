from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from sales.tests.sales_test_utilites import create_customers, create_user, create_boxes, create_contract, create_order
from sales.views import CustomerListView, BoxListCreateView, ContractListCreateView, OrdersListView


class CustomerListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_customers(count=10)
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

    def test_customer_list_count_is_10(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/sales/customer/all/')
        view = CustomerListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data['count'], 10)


class BoxListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        count = 10
        create_boxes(count)
        create_user()

    def test_box_list_view_authentication(self):
        response = self.client.get('/api/sales/box/all/')
        self.assertEqual(response.status_code, 401)

    def test_box_list_view_exists_at_desired_local(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/sales/box/all/')
        view = BoxListCreateView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_box_list_count_is_10(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/sales/box/all/')
        view = BoxListCreateView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data['count'], 10)


class ContractListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        count = 10
        create_contract(count)
        create_user()

    def test_contract_list_view_authentication(self):
        response = self.client.get('/api/sales/contract/all/')
        self.assertEqual(response.status_code, 401)

    def test_contract_list_view_exists_at_desired_local(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/sales/contract/all/')
        view = ContractListCreateView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_contract_list_count_is_10(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/sales/contract/all/')
        view = ContractListCreateView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data['count'], 10)


class OrderListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        count = 10
        create_order(count)
        create_user()

    def test_order_list_view_authentication(self):
        response = self.client.get('/api/sales/orders/all/')
        self.assertEqual(response.status_code, 401)

    def test_order_list_view_exists_at_desired_local(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/sales/orders/all/')
        view = OrdersListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_order_list_count_is_10(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/sales/orders/all/')
        view = OrdersListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data['count'], 10)
