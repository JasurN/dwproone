from django.http import HttpResponse
from .models import Paper, PaperConsumption, PaperIncoming, PaperIncomeRemainingFromProduction
from .serializers import PaperSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


"""Make paper consumption from request"""


def do_paper_consume(request):
    paperTempObj = Paper.objects.get(request.body.id)
    paperTempObj -= request.body.amount
    paperTempObj.save()
    paperConsumeObj = PaperConsumption(paper_id=request.body.id, paper_consumed=request.body.amount)
    paperConsumeObj.save()


"""Make Paper Income from request"""


def do_paper_income(request):
    paperTempObj = Paper.objects.get(request.body.id)
    paperTempObj += request.body.amount
    paperTempObj.save()
    paperIncomeObj = PaperIncoming(paper_id=request.body.id, paper_income=request.body.amount)
    paperIncomeObj.save()


"""Make paper income from production"""


def do_paper_income_remained_from_production(request):
    paperTempObj = Paper.objects.get(request.body.id)
    paperTempObj += request.body.amount
    paperTempObj.save()
    paperIncomeRemainingFromProductionObj = PaperIncomeRemainingFromProduction(paper_id=request.body.id,
                                                                               paper_income=request.body.amount)
    paperIncomeRemainingFromProductionObj.save()


def get_paper_values():
    paper = Paper.objects.values('id', 'paper_amount', 'company_id__name', 'paper_type_id__name',
                                 'paper_format_id__format', 'grammage_id__grammage',
                                 )
    return paper


@api_view(['GET', 'POST'])
def papers_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        paper = Paper.objects.all()
        serializer = PaperSerializer(paper, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
