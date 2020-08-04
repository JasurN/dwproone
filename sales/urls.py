from django.urls import path

from .views import AllOrdersListView, AllBoxListView, AllCustomerListView

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
]