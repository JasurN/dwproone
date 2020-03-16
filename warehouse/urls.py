from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [
    path('', views.papers_list),
    path('<int:pk>/', views.paper_operations),
    path('consumptions', views.get_all_paper_consumption),

]
