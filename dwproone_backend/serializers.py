from rest_framework import serializers
from .models import Paper, PaperIncoming, PaperConsumption


class PaperSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name')
    paper_type = serializers.CharField(source='paper_type.name')
    grammage = serializers.CharField(source='grammage.grammage')
    paper_format = serializers.CharField(source='paper_format.format')

    class Meta:
        model = Paper
        fields = ['id', 'paper_amount', 'paper_amount_remained_from_last_month', 'company_name', 'paper_type',
                  'paper_format', 'grammage']
