from django.urls import path

from .views import AllOrdersListView, AllBoxListView, AllCustomerListView, CustomerDetailView

app_name = 'sales'
# api/sales/
urlpatterns = [
    path('orders/all/', AllOrdersListView.as_view()),

]

urlpatterns += [
    path('box/all/', AllBoxListView.as_view()),
]

urlpatterns += [
    path('customer/all/', AllCustomerListView.as_view()),
    path('customer/all/<int:pk>/', CustomerDetailView.as_view())
]