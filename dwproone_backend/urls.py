from django.urls import path
from . import views

app_name = 'dwproone_backend'

urlpatterns = [
    path('', views.papers_list),
]