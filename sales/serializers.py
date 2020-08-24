from rest_framework import serializers

from sales.models import Order, Box, Customer, Contract, OrderDelivery


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 3


class AddOrderSerializer(serializers.ModelSerializer):
    contract_id = serializers.IntegerField(source='contract.id')
    box_id = serializers.IntegerField(source='box.id')

    class Meta:
        model = Order
        fields = ['contract_id', 'box_id', 'order_date', 'ship_date', 'quantity']


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


class OrderDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDelivery
        fields = '__all__'
        depth = 3
