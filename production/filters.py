from datetime import timedelta

import django_filters

from production.models import Production


class ProductionFilter(django_filters.FilterSet):
    scheduled_date = django_filters.DateFilter(field_name='scheduled_date', lookup_expr="exact")
    date_gte = django_filters.DateFilter(field_name='scheduled_date', lookup_expr='gte')
    date_lte = django_filters.DateFilter(field_name='scheduled_date', method='date_lte_plus_one_day')
    customer = django_filters.NumberFilter(field_name='order', lookup_expr="contract__customer_id__exact")

    def date_lte_plus_one_day(self, queryset, field_name, value):
        date_gte_plus_one_day = value + timedelta(days=+1)
        return queryset.filter(date__lte=date_gte_plus_one_day)

    class Meta:
        model = Production
        fields = ['scheduled_date', 'date_gte', 'date_lte', 'customer']
