# pagination.py
from collections import OrderedDict

import django_filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import json
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.core.exceptions import FieldDoesNotExist
from django.db.models.fields.related import ForeignObjectRel, OneToOneRel
from rest_framework.pagination import PageNumberPagination

from .models import Roll


class ReactAdminPagination(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "perPage"

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        item_starting_index = self.page.start_index() - 1
        item_ending_index = self.page.end_index() - 1

        content_range = "items {0}-{1}/{2}".format(
            item_starting_index, item_ending_index, count
        )

        headers = {"Content-Range": content_range}

        return Response(
            OrderedDict(
                [
                    ("count", count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("results", data),
                ]
            ),
            headers=headers,
        )


# filtering.py


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
    """
    See: https://github.com/tomchristie/django-rest-framework/issues/1005
    Extends OrderingFilter to support ordering by fields in related models
    using the Django ORM __ notation
    """

    def is_valid_field(self, model, field):
        """
        Return true if the field exists within the model (or in the related
        model specified using the Django ORM __ notation)
        """
        components = field.split('__', 1)
        try:
            field = model._meta.get_field(components[0])

            if isinstance(field, OneToOneRel):
                return self.is_valid_field(field.related_model, components[1])

            # reverse relation
            if isinstance(field, ForeignObjectRel):
                return self.is_valid_field(field.model, components[1])

            # foreign key
            if field.remote_field and len(components) == 2:
                return self.is_valid_field(field.related_model, components[1])

            return True
        except FieldDoesNotExist:
            return False

    def remove_invalid_fields(self, queryset, fields, ordering, view):
        return [term for term in fields
                if self.is_valid_field(queryset.model, term.lstrip('-'))]


class PageNumberWithPageSizePagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class PostFilter(django_filters.FilterSet):
    grammage = django_filters.NumberFilter(field_name='paper', lookup_expr="grammage_id__exact")

    class Meta:
        model = Roll
        fields = ["grammage", ]
