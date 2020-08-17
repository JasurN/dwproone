from warehouse.models import Paper_Format, Paper_Grammage, \
    Paper_Type, Paper_Producer, Paper


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
    return [Paper_Type.objects.create(name='KLB', code='K',
                                      description='Cellulose paper'),
            Paper_Type.objects.create(name='CMP', code='S',
                                      description='Local paper')]


def create_paper_producers(count):
    paper_producers = []
    for counter in range(count):
        paper_producers.append(
            Paper_Producer.objects.create(name=f'Producer {counter}',
                                          short_name=f'Prd {counter}')
        )
    return paper_producers


def create_papers(count):
    paper_types = create_paper_types()
    grammage = create_paper_grammage(count)
    formats = create_paper_formats(count)
    producers = create_paper_producers(count)
    papers = []
    for counter in range(count):
        papers.append(
            Paper.objects.create(grammage_id=grammage[counter].id,
                                 paper_type_id=paper_types[0].id,
                                 paper_format_id=formats[counter].id,
                                 company_id=producers[counter].id)
        )
    return papers
