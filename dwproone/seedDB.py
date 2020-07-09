from warehouse.models import Paper_Type, Paper_Format, Paper_Grammage, \
    Paper_Producer, Paper

Paper_Type.objects.bulk_create([
    Paper_Type(name="KLB", code="K", description="cellulose"),
    Paper_Type(name="CMP", code="S", description="corrugated paper"),
])

Paper_Format.objects.bulk_create([
    Paper_Format(format=800),
    Paper_Format(format=860),
    Paper_Format(format=910),
    Paper_Format(format=960),
    Paper_Format(format=1000),
    Paper_Format(format=1050),
    Paper_Format(format=1100),
    Paper_Format(format=1300),
    Paper_Format(format=1350),
    Paper_Format(format=1410),
    Paper_Format(format=1450),
    Paper_Format(format=1550),
])

Paper_Grammage.objects.bulk_create([
    Paper_Grammage(grammage=110),
    Paper_Grammage(grammage=115),
    Paper_Grammage(grammage=120),
    Paper_Grammage(grammage=125),
    Paper_Grammage(grammage=135),
    Paper_Grammage(grammage=140),
    Paper_Grammage(grammage=150),
])

Paper_Producer.objects.bulk_create([
    Paper_Producer(name="Bratsk", short_name='BK'),
    Paper_Producer(name="ENSO", short_name='ENS'),
    Paper_Producer(name="Namangan", short_name='NMG'),
    Paper_Producer(name="PTSBK", short_name='PBK'),
    Paper_Producer(name="BSQ", short_name='BSQ'),
    Paper_Producer(name="Nafis", short_name='NFS'),
])
# KLB - 1
# CMP - 2
# Paper.objects.bulk_create([
#         Paper(paper_type=Paper_Type, grammage=1, paper_format=1, company=1)
#     ])

# Measure_unit.objects.bulk_create([
#     Measure_unit(name='kilograms'),
#     Measure_unit(name='litres'),
#     Measure_unit(name='items')
# ])
