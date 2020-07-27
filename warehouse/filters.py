import json
from datetime import timedelta
from typing import Tuple, List

import django_filters
from django.db import models
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from .models import Roll, Roll_Consumption, Roll_Incoming


class PageNumberWithPageSizePagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class RelatedOrderingFilter(filters.OrderingFilter):
    _max_related_depth = 3

    @staticmethod
    def _get_verbose_name(field: models.Field, non_verbose_name: str) -> str:
        return field.verbose_name if hasattr(field, 'verbose_name') else non_verbose_name.replace('_', ' ')

    def _retrieve_all_related_fields(
            self,
            fields: Tuple[models.Field],
            model: models.Model,
            depth: int = 0
    ) -> List[tuple]:
        valid_fields = []
        if depth > self._max_related_depth:
            return valid_fields
        for field in fields:
            if field.related_model and field.related_model != model:
                rel_fields = self._retrieve_all_related_fields(
                    field.related_model._meta.get_fields(),
                    field.related_model,
                    depth + 1
                )
                for rel_field in rel_fields:
                    valid_fields.append((
                        f'{field.name}__{rel_field[0]}',
                        self._get_verbose_name(field, rel_field[1])
                    ))
            else:
                valid_fields.append((
                    field.name,
                    self._get_verbose_name(field, field.name),
                ))
        return valid_fields

    def get_valid_fields(self, queryset: models.QuerySet, view, context: dict = None) -> List[tuple]:
        valid_fields = getattr(view, 'ordering_fields', self.ordering_fields)
        if not valid_fields == '__all_related__':
            if not context:
                context = {}
            valid_fields = super().get_valid_fields(queryset, view, context)
        else:
            valid_fields = [
                *self._retrieve_all_related_fields(queryset.model._meta.get_fields(), queryset.model),
                *[(key, key.title().split('__')) for key in queryset.query.annotations]
            ]
        return valid_fields


class RollFilter(django_filters.FilterSet):
    grammage = django_filters.NumberFilter(field_name='paper', lookup_expr="grammage_id__exact")
    paper_format = django_filters.NumberFilter(field_name='paper', lookup_expr="paper_format_id__exact")
    paper_company = django_filters.NumberFilter(field_name='paper', lookup_expr="company_id__exact")

    class Meta:
        model = Roll
        fields = ["grammage", 'paper_format', 'paper_company']


class RollConsumptionFilter(django_filters.FilterSet):
    grammage = django_filters.NumberFilter(field_name='roll', lookup_expr="paper__grammage_id__exact")
    date_gte = django_filters.DateTimeFilter(field_name='date', lookup_expr='gte')
    date_lte = django_filters.DateTimeFilter(field_name='date', method='date_lte_plus_one_day')

    def date_lte_plus_one_day(self, queryset, field_name, value):
        date_gte_plus_one_day = value + timedelta(days=+1)
        return queryset.filter(date__lte=date_gte_plus_one_day)

    class Meta:
        model = Roll_Consumption
        fields = ["grammage", 'date_gte', 'date_lte']


class RollIncomeFilter(django_filters.FilterSet):
    grammage = django_filters.NumberFilter(field_name='roll', lookup_expr="paper__grammage_id__exact")
    date_gte = django_filters.DateTimeFilter(field_name='date', lookup_expr='gte')
    date_lte = django_filters.DateTimeFilter(field_name='date', method='date_lte_plus_one_day')

    def date_lte_plus_one_day(self, queryset, field_name, value):
        date_gte_plus_one_day = value + timedelta(days=+1)
        return queryset.filter(date__lte=date_gte_plus_one_day)

    class Meta:
        model = Roll_Incoming
        fields = ["grammage", 'date_gte', 'date_lte']
