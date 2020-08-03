from django.urls import path

from .views import AllOrdersListView

app_name = 'sales'
# api/sales/
urlpatterns = [
    path('orders/all/', AllOrdersListView.as_view()),
]
