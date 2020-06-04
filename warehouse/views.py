from rest_framework import status
from rest_framework.views import APIView
from .models import Paper, Roll
from .serializers import PaperSerializer, RollSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class RollView(APIView):
    serializer_class = RollSerializer

    def get(self, request):
        rolls = Roll.objects.all()
        rolls_serializer = RollSerializer(rolls, many=True)
        return Response(status=status.HTTP_200_OK, data=rolls_serializer.data)
#
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
#         """
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
