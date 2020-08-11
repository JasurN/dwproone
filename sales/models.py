from django.db import models


class Box(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    length = models.PositiveSmallIntegerField(help_text='box length')
    width = models.PositiveSmallIntegerField(help_text='box width')
    height = models.PositiveSmallIntegerField(help_text='box height')
    configuration = models.CharField(max_length=10, help_text='box configuration, KSS SSS KSSSK')
    dimension = models.CharField(max_length=20, help_text='box dimension length*width*height', default='1000x1000x1000')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.customer} {self.length}x{self.width}x{self.height} {self.configuration}"


class Customer(models.Model):
    name = models.CharField(help_text='customer name', max_length=100, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Contract(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=200, help_text='contract number DPC LB 190503')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.customer} {self.contract_number}"


class Order(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    order_date = models.DateField()
    ship_date = models.DateField()
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    remaining = models.PositiveSmallIntegerField()
    delivered = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.contract.customer} {self.contract.contract_number} " \
               f"{self.box.length}x{self.box.width}x{self.box.height} {self.box.configuration} " \
               f"{self.ship_date} {self.quantity} {self.remaining} {self.delivered}"
