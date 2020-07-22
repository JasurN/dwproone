from .models import Paper_Producer, Roll, Paper
from datetime import datetime


# Create paper id
def get_roll_id_and_instance_number(paper_producer_id, paper):
    paper_producer = Paper_Producer.objects.get(pk=paper_producer_id)
    today = datetime.today()
    paper_format = get_format_string_for_roll_id(paper[0].paper_format.format)
    try:
        roll = Roll.objects.filter(
            roll_id__contains=f'{paper_producer.short_name}{str(today.year)[-2:]}0{today.month}').order_by('-id')[0]
        return f'{paper_producer.short_name}{paper_format}{str(today.year)[-2:]}0{today.month}{roll.instance_number + 1}', \
               roll.instance_number + 1
    except IndexError:
        return f'{paper_producer.short_name}{paper_format}{str(today.year)[-2:]}0{today.month}1', 1


def get_format_string_for_roll_id(paper_format):
    if len(str(paper_format)) > 3:
        return paper_format
    else:
        return f'0{paper_format}'
