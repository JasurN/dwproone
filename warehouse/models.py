from django.db import models


class Paper_Producer(models.Model):
    name = models.CharField(help_text="raw material producer company name", max_length=150)
    # Todo: delete null true when make migration from 0
    short_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Paper_Type(models.Model):
    name = models.CharField(help_text="paper type name eg: CMP, KLB", max_length=20)
    code = models.CharField(help_text="paper type code eg: K, S, N or Ks", max_length=10)
    description = models.CharField(help_text="paper type description eg: corrugated paper, cellulose", max_length=100)

    def __str__(self):
        return self.name + " : " + self.code + " : " + self.description


class Paper_Format(models.Model):
    format = models.PositiveSmallIntegerField(help_text="format of paper")

    def __str__(self):
        return str(self.format)


# Paper Grammage model
class Paper_Grammage(models.Model):
    grammage = models.PositiveSmallIntegerField(help_text="grammage of paper")

    def __str__(self):
        return str(self.grammage)


class Paper(models.Model):
    paper_type = models.ForeignKey(Paper_Type, on_delete=models.CASCADE,
                                   help_text="paper type: KLB, CMP")
    grammage = models.ForeignKey(Paper_Grammage, on_delete=models.CASCADE,
                                 help_text=" paper grammage: 120-145")
    paper_format = models.ForeignKey(Paper_Format, on_delete=models.CASCADE,
                                     help_text="paper format: 800-1450")
    company = models.ForeignKey(Paper_Producer, on_delete=models.CASCADE,
                                help_text="company produced which paper ")

    class Meta:
        ordering = ['id']

    def __str__(self):
        """self.company.name -> refers to Company model name (e.g: ENZO or NAMANGAN)"""
        return self.company.name + " : " + self.paper_type.name + " : " + str(self.paper_format.format) + " : " + str(
            self.grammage.grammage)


class Roll(models.Model):
    roll_id = models.CharField(max_length=120)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    initial_weight = models.PositiveIntegerField()
    current_weight = models.PositiveIntegerField()
    income_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """self.company.name -> refers to Company model name (e.g: ENZO or NAMANGAN)"""
        return self.paper.company.name + " : " + self.paper.paper_type.name + " format: " + str(
            self.paper.paper_format.format) + " grammage: " + str(
            self.paper.grammage.grammage) + " current weight: " + str(
            self.current_weight) + " initial weight: " + str(self.initial_weight) + " income date: " + str(
            self.income_date)


class Roll_Consumption(models.Model):
    roll = models.ForeignKey(Roll, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)


class Roll_Incoming(models.Model):
    roll = models.ForeignKey(Roll, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)


class Roll_Return(models.Model):
    roll = models.ForeignKey(Roll, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

# class Measure_unit(models.Model):
#     name = models.CharField(max_length=10, help_text="Measurement unit kg or litre or ton")
#
#
# class Raw_material(models.Model):
#     name = models.CharField(max_length=100, help_text="Name of raw material vox, bura and etc")
#     amount = models.PositiveIntegerField(help_text="current amount of Raw Material")
#     amount_remained_from_last_month = models.PositiveIntegerField(
#         help_text="remained from last month amount of Raw Material")
#     measurement_id = models.ForeignKey(Measure_unit, on_delete=models.CASCADE,
#                                        help_text="foreign key id to measurement")
#
#
# class Raw_material_consumption(models.Model):
#     name = models.CharField(max_length=100, help_text="Raw material consumption")
#     amount = models.PositiveIntegerField(help_text="Amount of raw material consumption")
#     measurement_id = models.ForeignKey(Measure_unit, on_delete=models.CASCADE, help_text=" ")
#
#
# class Raw_material_incoming(models.Model):
#     name = models.CharField(max_length=100, help_text="Raw material income")
#     amount = models.PositiveIntegerField(help_text="Amount of raw material income")
#     amount_remained_from_last_month = models.PositiveIntegerField(help_text=" ")
#
#
# class Raw_material_remaining_from_production(models.Model):
#     name = models.CharField(max_length=100, help_text="Raw material income from production")
#     amount = models.PositiveIntegerField(help_text="Amount of raw material income from production")
#     measurement_id = models.ForeignKey(Measure_unit, on_delete=models.CASCADE, help_text=" ")
#
#
# # TODO: ОТХОД ВТУЛКА
# class Ink(models.Model):
#     name = models.CharField(max_length=100, help_text="")
#     amount = models.PositiveIntegerField(help_text="")
#     amount_remained_from_last_month = models.PositiveIntegerField(
#         help_text="")
#     measurement_id = models.ForeignKey(Measure_unit, on_delete=models.CASCADE,
#                                        help_text="")
#
#

# class Ink_consumption(models.Model):
#     name = models.CharField(max_length=100, help_text="")
#     amount = models.PositiveIntegerField(help_text="")
#     measurement_id = models.ForeignKey(Measure_unit, on_delete=models.CASCADE,
#                                        help_text="")
#
#

# class Ink_incoming(models.Model):
#     name = models.CharField(max_length=100, help_text="")
#     amount = models.PositiveIntegerField(help_text="")
#     measurement_id = models.ForeignKey(Measure_unit, on_delete=models.CASCADE,
#                                        help_text="")
