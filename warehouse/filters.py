import django_filters
from rest_framework.pagination import PageNumberPagination

from .models import Roll


class PageNumberWithPageSizePagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class RollFilter(django_filters.FilterSet):
    grammage = django_filters.NumberFilter(field_name='paper', lookup_expr="grammage_id__exact")
    paper_format = django_filters.NumberFilter(field_name='paper', lookup_expr="paper_format_id__exact")
    paper_company = django_filters.NumberFilter(field_name='paper', lookup_expr="company_id__exact")

    class Meta:
        model = Roll
        fields = ["grammage", 'paper_format', 'paper_company']
