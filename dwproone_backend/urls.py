from django.urls import path
from . import views

app_name = 'dwproone_backend'

urlpatterns = [
    path('', views.papers_list),
    path('<int:pk>/', views.paper_operations),
    path('<int:pk>/', views.paper_operations),

]
