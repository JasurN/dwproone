from django.db import models


class Box(models.Model):
    length = models.PositiveSmallIntegerField(help_text='box length')
    width = models.PositiveSmallIntegerField(help_text='box width')
    height = models.PositiveSmallIntegerField(help_text='box height')
    configuration = models.CharField(max_length=10, help_text='box configuration, KSS SSS KSSSK')


class Customer(models.Model):
    name = models.CharField(help_text='customer name')


class Contract(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=200, help_text='contract number DPC LB 190503')


# class Order(models.Model):
#     contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
#