from django.urls import path

from production.views import CorrugatorListView

app_name = 'production'
# api/sales/
urlpatterns = [
    path('corrugators/', CorrugatorListView.as_view()),

]

