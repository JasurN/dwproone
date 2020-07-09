from rest_framework import status, generics
from rest_framework.views import APIView

from .utility import get_roll_id_and_instance_number
from .react_admin_utilities import ReactAdminFilterBackend, RelatedOrderingFilter, RollFilter
from rest_framework.response import Response

from .models import Roll, Roll_Consumption, Paper_Format, Paper_Grammage, \
    Roll_Incoming, Roll_Return, Paper_Producer, Paper_Type, Paper
from .serializers import RollSerializer, RollConsumptionSerializer, \
    PaperFormatSerializer, PaperGrammageSerializer, RollIncomeSerializer, \
    RollReturnSerializer, PaperProducerSerializer, RollAddSerializer, PaperTypeSerializer


class RollsListCreateView(generics.ListCreateAPIView):
    queryset = Roll.objects.all().filter(current_weight__gt=0)
    serializer_class = RollSerializer
    # filter_backends = [
    #
    #                    filters.SearchFilter]
    # search_fields = ['roll_id', 'paper__paper_type__name', ]
    filterset_class = RollFilter
    ordering_fields = '__all__'

    def create(self, request, *args, **kwargs):
        roll_serializer = RollAddSerializer(data=request.data)
        roll_serializer.is_valid(raise_exception=True)
        paper = Paper.objects.get_or_create(company_id=roll_serializer.data['producer_id'],
                                            grammage_id=roll_serializer.data['grammage_id'],
                                            paper_format_id=roll_serializer.data['format_id'],
                                            paper_type_id=roll_serializer.data['paper_type_id'])
        roll_id, instance_number = get_roll_id_and_instance_number(paper[0].company_id, paper[0])
        roll = Roll(roll_id=roll_id,
                    paper=paper[0],
                    instance_number=instance_number,
                    initial_weight=roll_serializer.data['initial_weight'],
                    current_weight=roll_serializer.data['initial_weight'])
        roll_income = Roll_Incoming(roll=roll,
                                    amount=roll_serializer.data['initial_weight'])
        roll.save()
        roll_income.save()

        return Response(status=status.HTTP_201_CREATED)


class RollDetailView(APIView):
    serializer_class = RollSerializer

    def get(self, request, roll_id):
        roll = Roll.objects.get(pk=roll_id)
        rolls_serializer = RollSerializer(roll)
        return Response(status=status.HTTP_200_OK, data=rolls_serializer.data)


class RollsConsumptionListView(generics.ListAPIView):
    queryset = Roll_Consumption.objects.all()
    serializer_class = RollConsumptionSerializer
    ordering_fields = '__all__'


class MakeRollConsumption(APIView):
    def put(self, request, pk):
        roll = Roll.objects.get(pk=pk)
        roll.current_weight = 0
        roll_consumption = Roll_Consumption(roll=roll, amount=roll.initial_weight)
        roll_consumption.save()
        roll.save()
        rolls_serializer = RollSerializer(roll)
        return Response(status=status.HTTP_200_OK, data=rolls_serializer.data)


class RollsIncomeListView(generics.ListAPIView):
    queryset = Roll_Incoming.objects.all()
    serializer_class = RollIncomeSerializer
    ordering_fields = '__all__'


class RollsReturnListView(generics.ListAPIView):
    queryset = Roll_Return.objects.all()
    serializer_class = RollReturnSerializer
    ordering_fields = '__all__'


class PaperFormatListView(generics.ListAPIView):
    queryset = Paper_Format.objects.all().order_by('format')
    serializer_class = PaperFormatSerializer

    ordering_fields = '__all__'


class PaperFormatDetailView(APIView):
    serializer_class = PaperFormatSerializer

    def get(self, request, pk):
        paper_format = Paper_Format.objects.get(pk=pk)
        paper_format_serializer = PaperFormatSerializer(paper_format)
        return Response(status=status.HTTP_200_OK,
                        data=paper_format_serializer.data)


class PaperGrammageListView(generics.ListAPIView):
    queryset = Paper_Grammage.objects.all().order_by('grammage')
    serializer_class = PaperGrammageSerializer

    ordering_fields = '__all__'


class PaperGrammageDetailView(APIView):
    serializer_class = PaperGrammageSerializer

    def get(self, request, pk):
        paper_grammage = Paper_Grammage.objects.get(pk=pk)
        paper_grammage_serializer = PaperGrammageSerializer(paper_grammage)
        return Response(status=status.HTTP_200_OK,
                        data=paper_grammage_serializer.data)


class PaperProducerListView(generics.ListAPIView):
    queryset = Paper_Producer.objects.all()
    serializer_class = PaperProducerSerializer
    ordering_fields = '__all__'


class PaperProducerDetailView(APIView):
    serializer_class = PaperProducerSerializer

    def get(self, request, pk):
        paper_producer = Paper_Producer.objects.get(pk=pk)
        paper_producer_serializer = PaperProducerSerializer(paper_producer)
        return Response(status=status.HTTP_200_OK,
                        data=paper_producer_serializer.data)


class PaperTypesListView(generics.ListAPIView):
    queryset = Paper_Type.objects.all()
    serializer_class = PaperTypeSerializer
    ordering_fields = '__all__'


class PaperTypesDetailView(APIView):
    serializer_class = PaperTypeSerializer

    def get(self, request, pk):
        paper_types = Paper_Type.objects.get(pk=pk)
        paper_producer_serializer = PaperTypeSerializer(paper_types)
        return Response(status=status.HTTP_200_OK,
                        data=paper_producer_serializer.data)
# OLD CODE
# def paper_operation(pk, request_data):
#     if request_data['operation_type'] == "consume":
#         return make_paper_consume(pk, request_data['amount'])
#     elif request_data['operation_type'] == 'income':
#         return make_paper_income(pk, request_data['amount'])
#     elif request_data['operation_type'] == 'income_from_production':
#         return make_paper_income_remained_from_production(pk, request_data['amount'])
#
#
# """
# Make paper consumption from request
# """
#
#
# def make_paper_consume(paper_id, paper_consume_amount):
#     paperTempObj = Paper.objects.get(pk=paper_id)
#     paperTempObj.paper_amount -= int(paper_consume_amount)
#     paperTempObj.save()
#     paperConsumeObj = Paper_Consumption(paper_id=paper_id, amount=int(paper_consume_amount))
#     paperConsumeObj.save()
#     return paperTempObj
#
#
# """Make Paper Income from request"""
#
#
# def make_paper_income(paper_id, paper_income_amount):
#     paperTempObj = Paper.objects.get(pk=paper_id)
#     paperTempObj.paper_amount += int(paper_income_amount)
#     paperTempObj.save()
#     paperConsumeObj = Paper_Incoming(paper_id=paper_id, amount=int(paper_income_amount))
#     paperConsumeObj.save()
#     return paperTempObj
#
#
# """Make paper income from production"""
#
#
# def make_paper_income_remained_from_production(paper_id, paper_income_amount_from_production):
#     paperTempObj = Paper.objects.get(pk=paper_id)
#     paperTempObj.paper_amount += int(paper_income_amount_from_production)
#     paperTempObj.save()
#     paperConsumeObj = Paper_Income_Remaining_From_Production(paper_id=paper_id, amount=int(
#         paper_income_amount_from_production))
#     paperConsumeObj.save()
#     return paperTempObj
#
#
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def paper_consume_income_income_prod(request, pk):
#     """
#     Retrieve, update or delete a paper.
#     """
#     try:
#         Paper.objects.get(pk=pk)
#     except Paper.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         # serializer = SnippetSerializer(snippet)
#         return Response("GET PAPER/PK")
#     elif request.method == 'POST':
#         """
#         k"""
#         paperTempObj = paper_operation(pk, request.data)
#         return Response(PaperSerializer(paperTempObj).data)
#
#
# @api_view(['GET'])
# def get_all_paper_consumption(request):
#     if request.method == 'GET':
#         paper_consumption = Paper_Consumption.objects.all()
#         serializer = Paper_Consumption_Serializer(paper_consumption, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# def get_all_paper_income(request):
#     if request.method == 'GET':
#         paper_income = Paper_Incoming.objects.all()
#         serializer = Paper_Income_Serializer(paper_income, many=True)
#         return Response(serializer.data)
