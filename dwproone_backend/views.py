from django.http import HttpResponse
from .models import Paper, PaperConsumption, PaperIncoming, PaperIncomeRemainingFromProduction


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def do_paper_consume(request):
    paperTempObj = Paper.objects.get(request.body.id)
    paperTempObj -= request.body.amount
    paperTempObj.save()
    paperConsumeObj = PaperConsumption(paper_id=request.body.id, paper_consumed=request.body.amount)
    paperConsumeObj.save()


def do_paper_income(request):
    paperTempObj = Paper.objects.get(request.body.id)
    paperTempObj += request.body.amount
    paperTempObj.save()
    paperIncomeObj = PaperIncoming(paper_id=request.body.id, paper_income=request.body.amount)
    paperIncomeObj.save()


def do_paper_income_remained_from_production(request):
    paperTempObj = Paper.objects.get(request.body.id)
    paperTempObj += request.body.amount
    paperTempObj.save()
    paperIncomeRemainingFromProductionObj = PaperIncomeRemainingFromProduction(paper_id=request.body.id, paper_income=request.body.amount)
    paperIncomeRemainingFromProductionObj.save()
