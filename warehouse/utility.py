from itertools import chain

from django.db.models import Count, Sum

from .models import Paper_Producer, Roll, Paper_Type, Paper_Format
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
        return f'{paper_producer.short_name}{paper_format}{str(today.year)[-2:]}0{today.month}01', 1


# in 900
# return 0900
# in 1400
# out 1400
def get_format_string_for_roll_id(paper_format):
    if len(str(paper_format)) > 3:
        return paper_format
    else:
        return f'0{paper_format}'


# format instance
# in 1-9 return 0(1-9)
# in 10-99 return 10-99
def get_instance_number(instance_number):
    if len(str(instance_number)) > 1:
        return instance_number
    else:
        return f'0{instance_number}'


def get_total_roll_information():
    all_paper_types = Paper_Type.objects.all()
    all_paper_format = Paper_Format.objects.all()
    all_rolls = Roll.objects.filter(current_weight__gt=0)
    total_roll_info_by_format_and_type = []
    roll_id = 1
    for paper_type in all_paper_types:
        for paper_format in all_paper_format:
            temp_rolls = all_rolls.filter(paper__paper_format__format=paper_format.format,
                                          paper__paper_type__name=paper_type.name) \
                .aggregate(total_number_of_rolls=Count('current_weight'), total_weight_of_rolls=Sum('current_weight'))
            temp_rolls['paper_format'] = paper_format.format
            temp_rolls['paper_type'] = paper_type.name
            temp_rolls['id'] = roll_id
            roll_id += 1
            if temp_rolls['total_weight_of_rolls'] is None:
                temp_rolls['total_weight_of_rolls'] = 0
            total_roll_info_by_format_and_type.append(temp_rolls)
    return total_roll_info_by_format_and_type
