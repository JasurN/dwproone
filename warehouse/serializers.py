from rest_framework import serializers
from .models import Paper, Roll, Roll_Consumption, Paper_Format, Paper_Grammage, Roll_Incoming, Roll_Return, \
    Paper_Producer, Paper_Type


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
        fields = ['id', 'company_name', 'paper_type',
                  'paper_format', 'grammage']


class RollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roll
        fields = '__all__'
        depth = 2


class RollAddSerializer(serializers.ModelSerializer):
    producer_id = serializers.IntegerField(source='paper.company.id')
    format_id = serializers.IntegerField(source='paper.paper_format.id')
    grammage_id = serializers.IntegerField(source='paper.grammage.id')
    paper_type_id = serializers.IntegerField(source='paper.paper_type.id')

    class Meta:
        model = Roll
        fields = ['producer_id', 'format_id', 'grammage_id',
                  'paper_type_id', 'initial_weight']


class RollConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roll_Consumption
        fields = '__all__'
        depth = 3


class RollIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roll_Incoming
        fields = '__all__'
        depth = 3


class RollReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roll_Return
        fields = '__all__'
        depth = 3


class PaperFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper_Format
        fields = '__all__'


class PaperGrammageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper_Grammage
        fields = '__all__'


class PaperProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper_Producer
        fields = '__all__'


class PaperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper_Type
        fields = '__all__'


class RollTotalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    paper_format = serializers.IntegerField()
    paper_type = serializers.CharField()
    total_number_of_rolls = serializers.IntegerField()
    total_weight_of_rolls = serializers.IntegerField()

# class Paper_Consumption_Serializer(serializers.ModelSerializer):
#     """

#     """
#     producer_company = serializers.CharField(source='paper.company.name')
#     type = serializers.CharField(source='paper.paper_type.name')
#     grammage = serializers.CharField(source='paper.grammage.grammage')
#     format = serializers.CharField(source='paper.paper_format.format')
#
#     class Meta:
#         model = Paper_Consumption
#         fields = ['id', 'paper_id', 'producer_company', 'format',
#                   'type', 'grammage', 'amount', 'created']
#
#
# class Paper_Income_Serializer(serializers.ModelSerializer):
#     """

#     """
#     producer_company = serializers.CharField(source='paper.company.name')
#     type = serializers.CharField(source='paper.paper_type.name')
#     grammage = serializers.CharField(source='paper.grammage.grammage')
#     format = serializers.CharField(source='paper.paper_format.format')
#
#     class Meta:
#         model = Paper_Incoming
#         fields = ['id', 'paper_id', 'producer_company', 'format', 'type', 'grammage', 'amount', 'created']
