from warehouse.models import Paper_Type, Paper_Format, Paper_Grammage, Raw_Material_Producer_Company

Paper_Type.objects.bulk_create([
    Paper_Type(name="KLB", code="K", description="cellulose"),
    Paper_Type(name="CMP", code="S", description="corrugated paper"),
])

# Paper_Format.objects.bulk_create([
#     Paper_Format(format=800),
#     Paper_Format(format=860),
#     Paper_Format(format=910),
#     Paper_Format(format=960),
#     Paper_Format(format=1000),
#     Paper_Format(format=1050),
#     Paper_Format(format=1100),
#     Paper_Format(format=1300),
#     Paper_Format(format=1350),
#     Paper_Format(format=1410),
#     Paper_Format(format=1450),
#     Paper_Format(format=1550),
# ])
#
# Paper_Grammage.objects.bulk_create([
#     Paper_Grammage(grammage=110),
#     Paper_Grammage(grammage=115),
#     Paper_Grammage(grammage=120),
#     Paper_Grammage(grammage=125),
#     Paper_Grammage(grammage=135),
#     Paper_Grammage(grammage=140),
#     Paper_Grammage(grammage=150),
# ])
#
# Raw_Material_Producer_Company.objects.bulk_create([
#     Raw_Material_Producer_Company(name="Bratsk"),
#     Raw_Material_Producer_Company(name="ENSO"),
#     Raw_Material_Producer_Company(name="Namangan"),
#     Raw_Material_Producer_Company(name="PTSBK"),
#     Raw_Material_Producer_Company(name="BSQ"),
#     Raw_Material_Producer_Company(name="Nafis"),
# ])