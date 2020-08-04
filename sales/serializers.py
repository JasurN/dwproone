from rest_framework import serializers

from sales.models import Order


class AllOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 3
