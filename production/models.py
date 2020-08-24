from django.db import models

from sales.models import Order


class Production(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    production_order = models.PositiveSmallIntegerField(default=1)
    scheduled_date = models.DateField()
    final_producer_amount = models.PositiveSmallIntegerField(default=0)
    corrugator_amount = models.PositiveSmallIntegerField(default=0)
    corrugator_defect = models.PositiveSmallIntegerField(default=0)
    flex_amount = models.PositiveSmallIntegerField(default=0)
    flex_defect = models.PositiveSmallIntegerField(default=0)
    thompson_amount = models.PositiveSmallIntegerField(default=0)
    thompson_defect = models.PositiveSmallIntegerField(default=0)
    glue_amount = models.PositiveSmallIntegerField(default=0)
    glue_defect = models.PositiveSmallIntegerField(default=0)
    stitching_amount = models.PositiveSmallIntegerField(default=0)
    stitching_defect = models.PositiveSmallIntegerField(default=0)


class CorrugatorHistory(models.Model):
    production = models.ForeignKey(Production, on_delete=models.SET_NULL, null=True)
    produced_date = models.DateField()
    amount = models.PositiveSmallIntegerField(default=0)
    defect = models.PositiveSmallIntegerField(default=0)


class FlexHistory(models.Model):
    production = models.ForeignKey(Production, on_delete=models.SET_NULL, null=True)
    produced_date = models.DateField()
    amount = models.PositiveSmallIntegerField(default=0)
    defect = models.PositiveSmallIntegerField(default=0)


class GlueHistory(models.Model):
    production = models.ForeignKey(Production, on_delete=models.SET_NULL, null=True)
    produced_date = models.DateField()
    amount = models.PositiveSmallIntegerField(default=0)
    defect = models.PositiveSmallIntegerField(default=0)


class StitchingHistory(models.Model):
    production = models.ForeignKey(Production, on_delete=models.SET_NULL, null=True)
    produced_date = models.DateField()
    amount = models.PositiveSmallIntegerField(default=0)
    defect = models.PositiveSmallIntegerField(default=0)
