from django.contrib import admin
from .models import Paper_Format, Paper_Type, Paper_Grammage, Paper, Paper_Producer

admin.site.register(Paper_Format)
admin.site.register(Paper_Type)
admin.site.register(Paper_Grammage)
admin.site.register(Paper)
admin.site.register(Paper_Producer)

# Register your models here.
