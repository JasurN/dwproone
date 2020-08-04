from rest_framework import generics

from sales.models import Order, Box, Customer
from sales.serializers import AllOrdersSerializer, AllBoxSerializer, AllCustomerSerializer


class AllOrdersListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = AllOrdersSerializer


class AllBoxListView(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = AllBoxSerializer


class AllCustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = AllCustomerSerializer
