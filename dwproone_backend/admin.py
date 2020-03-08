from django.contrib import admin
from .models import PaperFormat, PaperType, PaperGrammage, Paper, Company, PaperConsumption, PaperIncoming, \
    PaperIncomeRemainingFromProduction

admin.site.register(PaperFormat)
admin.site.register(PaperType)
admin.site.register(PaperGrammage)
admin.site.register(Paper)
admin.site.register(Company)
admin.site.register(PaperConsumption)

# Register your models here.
