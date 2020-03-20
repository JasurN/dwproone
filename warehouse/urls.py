from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [
    path('', views.papers_list),
    path('<int:pk>/', views.paper_consume_income_income_prod),
    path('consumption', views.get_all_paper_consumption),
    path('income', views.get_all_paper_income),

]
