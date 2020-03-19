from rest_framework import serializers
from .models import Paper, Paper_Incoming, Paper_Consumption


class PaperSerializer(serializers.ModelSerializer):
    """
    Paper Serializer,
        company_name = serializers.CharField(source='company.name') ->
        -> it gives name of company instead of id.
        source = 'company.name' references to Paper.company and it references to
        Company Model Paper.company(Company).name

    """
    company_name = serializers.CharField(source='company.name')
    paper_type = serializers.CharField(source='paper_type.name')
    grammage = serializers.CharField(source='grammage.grammage')
    paper_format = serializers.CharField(source='paper_format.format')

    class Meta:
        model = Paper
        fields = ['id', 'paper_amount', 'paper_amount_remained_from_last_month', 'company_name', 'paper_type',
                  'paper_format', 'grammage']


class Paper_Consumption_Serializer(serializers.ModelSerializer):
    """
    TODO: Write doc
    """
    producer_company = serializers.CharField(source='paper.company.name')
    type = serializers.CharField(source='paper.paper_type.name')
    grammage = serializers.CharField(source='paper.grammage.grammage')
    format = serializers.CharField(source='paper.paper_format.format')

    class Meta:
        model = Paper_Consumption
        fields = ['id', 'paper_id', 'producer_company', 'format', 'type', 'grammage', 'paper_consumed', 'created']
