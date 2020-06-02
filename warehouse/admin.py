from django.contrib import admin
from .models import Paper_Format, Paper_Type, Paper_Grammage, Paper, \
    Paper_Producer, Roll, Roll_Consumption, Roll_Incoming, Roll_Return

admin.site.register(Paper_Format)


class PaperTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'description')


admin.site.register(Paper_Type, PaperTypeAdmin)
admin.site.register(Paper_Grammage)


class Paper_Producer_Admin(admin.ModelAdmin):
    list_display = ('name', 'short_name')


admin.site.register(Paper_Producer, Paper_Producer_Admin)


class RollInline(admin.TabularInline):
    model = Roll


@admin.register(Paper)
class Paper_Admin(admin.ModelAdmin):
    list_display = ('get_company_name', 'get_paper_type', 'get_paper_format', 'get_paper_grammage')
    inlines = [RollInline]


class Roll_Admin(admin.ModelAdmin):
    list_display = ('roll_id', 'initial_weight', 'current_weight', 'income_date', 'get_company_name',
                    'get_paper_type', 'get_paper_format', 'get_paper_grammage')


admin.site.register(Roll, Roll_Admin)
admin.site.register(Roll_Consumption)
admin.site.register(Roll_Incoming)
admin.site.register(Roll_Return)
