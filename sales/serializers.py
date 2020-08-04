from rest_framework import serializers

from sales.models import Order, Box, Customer


class AllOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 3


class AllBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'
        depth = 2


class AllCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        depth = 2
