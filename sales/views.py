from rest_framework import generics

from sales.models import Order
from sales.serializers import AllOrdersSerializer


class AllOrdersListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = AllOrdersSerializer
