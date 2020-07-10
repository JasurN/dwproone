import json
from typing import Tuple, List

import django_filters
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from .models import Roll, Roll_Consumption


class PageNumberWithPageSizePagination(PageNumberPagination):
    page_size_query_param = 'page_size'


def sort_queryset(queryset, value):
    try:
        [field, order] = json.loads(value)
    except json.decoder.JSONDecodeError:
        return queryset

    if field and order:
        return queryset.order_by(f"-{field}" if order == "DESC" else field)

    return queryset


def filter_queryset_for_multiple(queryset, key, value):
    filter_params = {key: value.split(",")}
    return queryset.filter(**filter_params)


def filter_queryset_for_nullable(queryset, key, value):
    nullable = True if value == "true" else False if value == "false" else None

    if nullable is None:
        return queryset

    filter_params = {key: nullable}
    return queryset.filter(**filter_params)


def filter_queryset_for_reference(queryset, key, value):
    f = True if value == "true" else False if value == "false" else value

    filter_params = {key: f}
    return queryset.filter(**filter_params)


class ReactAdminFilterBackend(DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        for key, value in request.query_params.items():
            if key == "sort" and value:
                queryset = sort_queryset(queryset, value)
            elif key.endswith("__in"):
                queryset = filter_queryset_for_multiple(queryset, key, value)
            elif key.endswith("__isnull"):
                queryset = filter_queryset_for_nullable(queryset, key, value)
            elif "__" in key:
                queryset = filter_queryset_for_reference(queryset, key, value)

        return {"data": request.query_params, "queryset": queryset, "request": request}


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
    date_lte = django_filters.DateTimeFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Roll_Consumption
        fields = ["grammage", 'date_gte']
