from django.contrib import admin
from .models import Paper_Format, Paper_Type, Paper_Grammage, Paper, \
    Paper_Producer, Roll, Roll_Consumption, Roll_Incoming, Roll_Return

admin.site.register(Paper_Format)
admin.site.register(Paper_Type)
admin.site.register(Paper_Grammage)
admin.site.register(Paper)
admin.site.register(Paper_Producer)
admin.site.register(Roll)
admin.site.register(Roll_Consumption)
admin.site.register(Roll_Incoming)
admin.site.register(Roll_Return)

# Register your models here.
