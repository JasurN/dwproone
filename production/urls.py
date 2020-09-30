from django.urls import path

from production.views import ProductionListCreateView

app_name = 'production'
# api/production/
urlpatterns = [
    path('', ProductionListCreateView.as_view()),
]
