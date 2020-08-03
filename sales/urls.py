from django.urls import path
from . import views

app_name = 'sales'
# api/sales/
urlpatterns = [
    path('', views.index),
]
