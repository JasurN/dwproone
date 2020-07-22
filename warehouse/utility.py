from .models import Paper_Producer, Roll, Paper
from datetime import datetime


# Create paper id
# in paper, paper producer id
# filters roll object with (producer short name + paper format + year (20) + month(07) and get last element
# if no element exception returns
# if element exists return roll id - SMR090020071
def get_roll_id_and_instance_number(paper_producer_id, paper):
    paper_producer = Paper_Producer.objects.get(pk=paper_producer_id)
    today = datetime.today()
    paper_format = get_format_string_for_roll_id(paper[0].paper_format.format)
    try:
        roll = Roll.objects.filter(
            roll_id__contains=f'{paper_producer.short_name}{paper_format}{str(today.year)[-2:]}0{today.month}').order_by(
            '-id')[0]
        instance_number = get_instance_number(roll.instance_number + 1)
        return f'{paper_producer.short_name}{paper_format}' \
               f'{str(today.year)[-2:]}0{today.month}{instance_number}', \
               roll.instance_number + 1
    except IndexError:
        return f'{paper_producer.short_name}{paper_format}{str(today.year)[-2:]}0{today.month}1', 1


# in 900
# return 0900
# in 1400
# out 1400
def get_format_string_for_roll_id(paper_format):
    if len(str(paper_format)) > 3:
        return paper_format
    else:
        return f'0{paper_format}'


def get_instance_number(instance_number):
    if len(str(instance_number)) > 1:
        return instance_number
    else:
        return f'0{instance_number}'
