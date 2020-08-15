from warehouse.models import Paper_Format, Paper_Grammage, Paper_Type


def create_paper_formats(count):
    paper_formats = []
    initial_format = 950
    for counter in range(count):
        paper_formats.append(
            Paper_Format.objects.create(format=initial_format)
        )
        initial_format = initial_format + 50
    return paper_formats


def create_paper_grammage(count):
    paper_grammage = []
    initial_grammage = 100
    for counter in range(count):
        paper_grammage.append(
            Paper_Grammage.objects.create(grammage=initial_grammage)
        )
        initial_grammage = initial_grammage + 10
    return paper_grammage


def create_paper_types():
    return [Paper_Type.objects.create(name='KLB', code='K', description='Cellulose paper'),
            Paper_Type.objects.create(name='CMP', code='S', description='Local paper')]
