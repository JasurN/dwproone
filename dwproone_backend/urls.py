from django.urls import path
from . import views

app_name = 'dwproone_backend'

urlpatterns = [
    # ex: /polls/
    path('', views.index),
]