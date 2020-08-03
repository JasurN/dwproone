from django.contrib import admin

from .models import Box, Contract, Customer, Order

admin.site.register(Box)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Contract)
# Register your models here.
