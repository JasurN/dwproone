import django_filters

from production.models import Production


class ProductionFilter(django_filters.FilterSet):
    scheduled_date = django_filters.DateFilter(field_name='scheduled_date', lookup_expr="exact")

    class Meta:
        model = Production
        fields = ['scheduled_date']
