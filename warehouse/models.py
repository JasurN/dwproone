from django.db import models


class Paper_Producer(models.Model):
    name = models.CharField(help_text="raw material producer company name", max_length=150)

    def __str__(self):
        return self.name


# Paper type model
class Paper_Type(models.Model):
    name = models.CharField(help_text="paper type name eg: CMP, KLB", max_length=20)
    code = models.CharField(help_text="paper type code eg: K, S, N or Ks", max_length=10)
    description = models.CharField(help_text="paper type description eg: corrugated paper, cellulose", max_length=100)

    def __str__(self):
        return self.name + " : " + self.code + " : " + self.description


# Paper format model
class Paper_Format(models.Model):
    format = models.PositiveSmallIntegerField(help_text="format of paper")

    def __str__(self):
        return str(self.format)


# Paper Grammage model
class Paper_Grammage(models.Model):
    grammage = models.PositiveSmallIntegerField(help_text="grammage of paper")

    def __str__(self):
        return str(self.grammage)


# Main model for Paper information
class Paper(models.Model):
    paper_type = models.ForeignKey(Paper_Type, on_delete=models.CASCADE,
                                   help_text="paper type: KLB, CMP")
    grammage = models.ForeignKey(Paper_Grammage, on_delete=models.CASCADE,
                                 help_text=" paper grammage: 120-145")
    paper_format = models.ForeignKey(Paper_Format, on_delete=models.CASCADE,
                                     help_text="paper format: 800-1450")
    company = models.ForeignKey(Paper_Producer, on_delete=models.CASCADE,
                                help_text="company produced which paper ")
    paper_amount = models.PositiveIntegerField(help_text="current amount of paper")
    paper_amount_remained_from_last_month = models.PositiveIntegerField(
        help_text="amount of paper remained from last month")

    class Meta:
        ordering = ['id']
    # def __str__(self):
    #     """self.company.name -> refers to Company model name (e.g: ENZO or NAMANGAN)"""
    #     return self.company.name + " : " + self.paper_type.name + " : " + str(self.paper_format.format) + " : " + str(
    #         self.grammage.grammage) + " : paper_amount = " + str(self.paper_amount)


# model for Paper consumption
class Paper_Consumption(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE,
                              help_text="Paper that is Consumed",
                              default=1)
    paper_consumed = models.PositiveIntegerField(help_text="consumed amount of paper",
                                                 default=0)
    created = models.DateTimeField(auto_now_add=True)


# model for Paper incoming
class Paper_Incoming(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE,
                              help_text="Paper that is Income",
                              default=1)
    paper_income = models.PositiveIntegerField(help_text="income amount of paper",
                                               default=0)

    created = models.DateTimeField(auto_now_add=True)


# model for Paper incoming from production. left from production
class Paper_Income_Remaining_From_Production(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE,
                              help_text="Paper that is Income from production",
                              default=1)
    paper_income_production = models.PositiveIntegerField(help_text="income amount of paper from production",
                                                          default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True)


# model for Measurement unit E.g kg, or lipaper_consumed = models.PositiveIntegerFieldtre
class Measure_unit(models.Model):
    name = models.CharField(max_length=10, help_text="Measurement unit kg or litre or ton")


# TODO: write doc and __str__
class Raw_material(models.Model):
    name = models.CharField(max_length=100, help_text="Name of raw material vox, bura and etc")
    amount = models.PositiveIntegerField(help_text="current amount of Raw Material")
    amount_remained_from_last_month = models.PositiveIntegerField(
        help_text="remained from last month amount of Raw Material")
    measurement_id = models.ForeignKey(Measure_unit, on_delete=models.CASCADE,
                                       help_text="foreign key id to measurement")


# TODO: write doc and __str__
class Raw_material_consumption(models.Model):
    name = models.CharField(max_length=100, help_text=" ")
    amount = models.PositiveIntegerField(help_text=" ")
    measurement_id = models.ForeignKey(Measure_unit, on_delete=models.CASCADE, help_text=" ")


# TODO: write doc and __str__
class Raw_material_incoming(models.Model):
    name = models.CharField(max_length=100, help_text=" ")
    amount = models.PositiveIntegerField(help_text=" ")
    amount_remained_from_last_month = models.PositiveIntegerField(help_text=" ")


# TODO: write doc and __str__
class Raw_material_remaining_from_production(models.Model):
    name = models.CharField(max_length=100, help_text=" ")
    amount = models.PositiveIntegerField(help_text=" ")
    measurement_id = models.ForeignKey(Measure_unit, on_delete=models.CASCADE, help_text=" ")


# TODO: ОТХОД ВТУЛКА
class Ink(models.Model):
    name = models.CharField(max_length=100, help_text="")
    amount = models.PositiveIntegerField(help_text="")
    amount_remained_from_last_month = models.PositiveIntegerField(
        help_text="")
    measurement_id = models.ForeignKey(Measure_unit, on_delete=models.CASCADE,
                                       help_text="")


# TODO: write doc and __str__
class Ink_consumption(models.Model):
    name = models.CharField(max_length=100, help_text="")
    amount = models.PositiveIntegerField(help_text="")
    measurement_id = models.ForeignKey(Measure_unit, on_delete=models.CASCADE,
                                       help_text="")


# TODO: write doc and __str__
class Ink_incoming(models.Model):
    name = models.CharField(max_length=100, help_text="")
    amount = models.PositiveIntegerField(help_text="")
    measurement_id = models.ForeignKey(Measure_unit, on_delete=models.CASCADE,
                                       help_text="")
