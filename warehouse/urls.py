from django.urls import path
from .views import RollView

app_name = 'warehouse'

urlpatterns = [
    path('rolls', RollView.as_view()),
]
