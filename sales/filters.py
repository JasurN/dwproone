from datetime import timedelta

import django_filters

from sales.models import OrderDelivery


class OrderDeliveryFilter(django_filters.FilterSet):
    date_gte = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_lte = django_filters.DateFilter(field_name='date', method='date_lte_plus_one_day')

    def date_lte_plus_one_day(self, queryset, field_name, value):
        date_gte_plus_one_day = value + timedelta(days=+1)
        return queryset.filter(date__lte=date_gte_plus_one_day)

    class Meta:
        model = OrderDelivery
        fields = ['date_gte', 'date_lte']
