from rest_framework import serializers

from production.models import Production


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__'
        depth = 4


class AddProductionSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='order.id')

    class Meta:
        model = Production
        fields = ['order_id', 'scheduled_date', 'production_order']
