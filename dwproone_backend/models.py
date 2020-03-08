from django.db import models


# Company main model
class Company(models.Model):
    name = models.CharField("company name", max_length=150)


# Paper type model
class PaperType(models.Model):
    name = models.CharField("paper type name eg: CMP, KLB", max_length=20)
    code = models.CharField("paper type code eg: K, S, N or Ks", max_length=10)
    description = models.CharField("paper type description eg: corrugated paper, cellulose", max_length=100)


# Paper format model
class PaperFormat(models.Model):
    format = models.PositiveSmallIntegerField("format of paper")


# Paper Grammage model
class PaperGrammage(models.Model):
    grammage = models.PositiveSmallIntegerField("grammage of paper")


# Main model for Paper information
class Paper(models.Model):
    paper_type = models.ForeignKey(PaperType, on_delete=models.CASCADE,
                                   verbose_name="paper type: KLB, CMP")
    grammage = models.ForeignKey(PaperGrammage, on_delete=models.CASCADE,
                                 verbose_name=" paper grammage: 120-145")
    paper_format = models.ForeignKey(PaperFormat, on_delete=models.CASCADE,
                                     verbose_name="paper format: 800-1450")
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name="company produced which paper ")
    paper_amount = models.PositiveIntegerField("current amount of paper")
    paper_amount_remained_from_last_month = models.PositiveIntegerField("amount of paper remained from last month")


# model for Paper consumption
class PaperConsumption(models.Model):
    pass


# model for Paper incoming
class PaperIncoming(models.Model):
    pass


# model for Paper incoming from production. left from production
class PaperIncomeRemainingFromProduction(models.Model):
    pass


# PaperType.objects.bulk_create([
#     PaperType(name="KLB", code="K", description="cellulose"),
#     PaperType(name="CMP", code="S", description="corrugated paper"),
# ])
#
# PaperFormat.objects.bulk_create([
#     PaperFormat(format=800),
#     PaperFormat(format=860),
#     PaperFormat(format=910),
#     PaperFormat(format=960),
#     PaperFormat(format=1000),
#     PaperFormat(format=1050),
#     PaperFormat(format=1100),
#     PaperFormat(format=1300),
#     PaperFormat(format=1350),
#     PaperFormat(format=1410),
#     PaperFormat(format=1450),
#     PaperFormat(format=1550),
# ])
#
# PaperGrammage.objects.bulk_create([
#     PaperGrammage(grammage=110),
#     PaperGrammage(grammage=115),
#     PaperGrammage(grammage=120),
#     PaperGrammage(grammage=125),
#     PaperGrammage(grammage=135),
#     PaperGrammage(grammage=140),
#     PaperGrammage(grammage=150),
# ])

# Company.objects.bulk_create([
#     Company(name="Bratsk"),
#     Company(name="ENSO"),
#     Company(name="Namangan"),
#     Company(name="PTSBK"),
#     Company(name="BSQ"),
#     Company(name="Nafis"),
# ])

# Paper.objects.bulk_create([
#     print(PaperType.objects.get(name='KLP'))
#
# ])
