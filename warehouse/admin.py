from django.contrib import admin
from .models import Paper_Format, Paper_Type, Paper_Grammage, Paper, Raw_Material_Producer_Company, Paper_Consumption, Paper_Incoming, \
    Paper_Income_Remaining_From_Production

admin.site.register(Paper_Format)
admin.site.register(Paper_Type)
admin.site.register(Paper_Grammage)
admin.site.register(Paper)
admin.site.register(Raw_Material_Producer_Company)
admin.site.register(Paper_Consumption)

# Register your models here.
