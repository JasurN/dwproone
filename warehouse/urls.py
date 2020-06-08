from django.urls import path
from .views import RollView, RollDetailView

app_name = 'warehouse'

urlpatterns = [
    path('rolls/', RollView.as_view()),
    path('rolls/<int:roll_id>/', RollDetailView.as_view())
]
