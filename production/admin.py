from django.contrib import admin

from production.models import Production, CorrugatorHistory, \
    FlexHistory, GlueHistory, StitchingHistory

admin.site.register(Production)
admin.site.register(CorrugatorHistory)
admin.site.register(FlexHistory)
admin.site.register(GlueHistory)
admin.site.register(StitchingHistory)
