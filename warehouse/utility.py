from .models import Paper_Producer, Roll
from datetime import datetime


def get_roll_id_and_instance_number(paper_producer_id, paper):
    paper_producer = Paper_Producer.objects.get(pk=paper_producer_id)
    today = datetime.today()
    try:
        roll = Roll.objects.filter(paper=paper).order_by('-id')[0]
        return f'{paper_producer.short_name}{str(today.year)[-2:]}0{today.month}{roll.instance_number + 1}', \
               roll.instance_number + 1
    except Roll:
        return f'test', 0
