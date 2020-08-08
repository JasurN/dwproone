from rest_framework import serializers

from sales.models import Order, Box, Customer, Contract


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 3


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'
        depth = 2


class AddBoxSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(source='customer.id')

    class Meta:
        model = Box
        fields = ['customer_id', 'length', 'width', 'height', 'configuration']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        depth = 2


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
        depth = 2
