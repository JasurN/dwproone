from rest_framework import serializers
from .models import Paper, PaperIncoming, PaperConsumption


class PaperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paper
        fields = ['id', 'paper_amount', 'paper_amount_remained_from_last_month', 'company', 'paper_type_id',
                  'paper_format_id', 'grammage_id']
