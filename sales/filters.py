from datetime import timedelta

import django_filters

from sales.models import OrderDelivery, Order


class OrderDeliveryFilter(django_filters.FilterSet):
    date_gte = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_lte = django_filters.DateFilter(field_name='date', method='date_lte_plus_one_day')
    customer = django_filters.NumberFilter(field_name='order', lookup_expr="contract__customer_id__exact")

    def date_lte_plus_one_day(self, queryset, field_name, value):
        date_gte_plus_one_day = value + timedelta(days=+1)
        return queryset.filter(date__lte=date_gte_plus_one_day)

    class Meta:
        model = OrderDelivery
        fields = ['date_gte', 'date_lte', 'customer']


class OrderFilter(django_filters.FilterSet):
    customer = django_filters.NumberFilter(field_name='contract', lookup_expr="customer_id__exact")

    class Meta:
        model = Order
        fields = ['customer']
