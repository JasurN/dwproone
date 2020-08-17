from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from sales.tests.sales_test_utilites import create_user
from warehouse.tests.warehouse_test_utilities \
    import create_paper_formats, create_paper_grammage, create_paper_types, \
    create_paper_producers, create_papers
from warehouse.views import PaperFormatListView, \
    PaperGrammageListView, PaperTypesListView, PaperProducerListView, PaperListView


class PaperFormatListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        count = 10
        create_paper_formats(count)
        create_user()

    def test_paper_format_list_view_authentication(self):
        response = self.client.get('/api/warehouse/papers/formats/')
        self.assertEqual(response.status_code, 401)

    def test_paper_format_list_view_exists_at_desired_local(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/warehouse/papers/formats/')
        view = PaperFormatListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_paper_format_list_count_is_10(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/warehouse/papers/formats/')
        view = PaperFormatListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data['count'], 10)


class PaperGrammageListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        count = 10
        create_paper_grammage(count)
        create_user()

    def test_paper_grammage_list_view_authentication(self):
        response = self.client.get('/api/warehouse/papers/grammage/')
        self.assertEqual(response.status_code, 401)

    def test_paper_grammage_list_view_exists_at_desired_local(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/warehouse/papers/grammage/')
        view = PaperGrammageListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_paper_grammage_list_count_is_10(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/warehouse/papers/grammage/')
        view = PaperGrammageListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data['count'], 10)


class PaperTypeListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_paper_types()
        create_user()

    def test_paper_type_list_view_authentication(self):
        response = self.client.get('/api/warehouse/papers/types/')
        self.assertEqual(response.status_code, 401)

    def test_paper_type_list_view_exists_at_desired_local(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/warehouse/papers/types/')
        view = PaperTypesListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_paper_type_list_count_is_10(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/warehouse/papers/types/')
        view = PaperTypesListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data['count'], 2)


class PaperProducerListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        count = 10
        create_paper_producers(count)
        create_user()

    def test_paper_producer_list_view_authentication(self):
        response = self.client.get('/api/warehouse/papers/producers/')
        self.assertEqual(response.status_code, 401)

    def test_paper_producer_list_view_exists_at_desired_local(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/warehouse/papers/producers/')
        view = PaperProducerListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_paper_producer_list_count_is_10(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/warehouse/papers/producers/')
        view = PaperProducerListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data['count'], 10)


class PaperListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        count = 10
        create_papers(count)
        create_user()

    def test_papers_list_view_authentication(self):
        response = self.client.get('/api/warehouse/papers/all/')
        self.assertEqual(response.status_code, 401)

    def test_paper_format_list_view_exists_at_desired_local(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/warehouse/papers/all/')
        view = PaperListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_paper_format_list_count_is_10(self):
        factory = APIRequestFactory()
        user = User.objects.get(username='testuser1')
        request = factory.get('/api/warehouse/papers/all/')
        view = PaperListView.as_view()
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data['count'], 10)
