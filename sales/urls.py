from django.urls import path

from .views import OrdersListView, BoxListCreateView, CustomerListView, CustomerDetailView, ContractListCreateView, \
    ContractDetailView, BoxDetailView, OrderDetailView, OrderDeliveryListView

app_name = 'sales'
# api/sales/
urlpatterns = [
    path('orders/all/', OrdersListView.as_view()),
    path('orders/all/<int:pk>/', OrderDetailView.as_view())
]

urlpatterns += [
    path('box/all/', BoxListCreateView.as_view()),
    path('box/all/<int:pk>/', BoxDetailView.as_view())
]

urlpatterns += [
    path('customer/all/', CustomerListView.as_view()),
    path('customer/all/<int:pk>/', CustomerDetailView.as_view())
]

urlpatterns += [
    path('contract/all/', ContractListCreateView.as_view()),
    path('contract/all/<int:pk>/', ContractDetailView.as_view())
]

urlpatterns = [
    path('orders/delivery/all/', OrderDeliveryListView.as_view()),
]