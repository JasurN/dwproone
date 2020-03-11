from .models import Paper, PaperConsumption, PaperIncoming, PaperIncomeRemainingFromProduction
from .serializers import PaperSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return Response("Hello, world. You're at the polls index.")


def paper_operation(pk, request_data):
    if request_data['operation_type'] == "consume":
        return do_paper_consume(pk, request_data['consume_amount'])
    elif request_data['operation_type'] == 'income':
        return do_paper_income(pk, request_data['income_amount'])
    elif request_data['operation_type'] == 'income_from_production':
        return do_paper_income_remained_from_production(pk, request_data['income_amount'])


"""
Make paper consumption from request
"""


def do_paper_consume(paper_id, paper_consume_amount):
    paperTempObj = Paper.objects.get(pk=paper_id)
    paperTempObj.paper_amount -= int(paper_consume_amount)
    paperTempObj.save()
    paperConsumeObj = PaperConsumption(paper_id=paper_id, paper_consumed=int(paper_consume_amount))
    paperConsumeObj.save()
    return paperTempObj


"""Make Paper Income from request"""


def do_paper_income(paper_id, paper_income_amount):
    paperTempObj = Paper.objects.get(pk=paper_id)
    paperTempObj.paper_amount += int(paper_income_amount)
    paperTempObj.save()
    paperConsumeObj = PaperIncoming(paper_id=paper_id, paper_income=int(paper_income_amount))
    paperConsumeObj.save()
    return paperTempObj


"""Make paper income from production"""


def do_paper_income_remained_from_production(paper_id, paper_income_amount_from_production):
    paperTempObj = Paper.objects.get(pk=paper_id)
    paperTempObj.paper_amount += int(paper_income_amount_from_production)
    paperTempObj.save()
    paperConsumeObj = PaperIncomeRemainingFromProduction(paper_id=paper_id, paper_income_production=int(
        paper_income_amount_from_production))
    paperConsumeObj.save()
    return paperTempObj


@api_view(['GET', 'POST'])
def papers_list(request, format=None):
    """
    List all papers
    """
    if request.method == 'GET':
        paper = Paper.objects.all()
        serializer = PaperSerializer(paper, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response("Hello from server")
    #     serializer = PaperSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def paper_operations(request, pk):
    """
    Retrieve, update or delete a paper.
    """
    try:
        Paper.objects.get(pk=pk)
    except Paper.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # serializer = SnippetSerializer(snippet)
        return Response("GET PAPER/PK")
    elif request.method == 'POST':
        """
        TODO: WRITE DOC
        """
        paperTempObj = paper_operation(pk, request.data)
        return Response(PaperSerializer(paperTempObj).data)
    # elif request.method == 'PUT':
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # elif request.method == 'DELETE':
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
