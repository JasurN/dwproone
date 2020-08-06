from rest_framework import generics, status
from rest_framework.response import Response

from sales.models import Order, Box, Customer
from sales.serializers import AllOrdersSerializer, BoxSerializer, CustomerSerializer, AddBoxSerializer


class AllOrdersListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = AllOrdersSerializer


class AllBoxListView(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

    def create(self, request, *args, **kwargs):
        box_serializer = AddBoxSerializer(data=request.data)
        box_serializer.is_valid(raise_exception=True)
        box = Box.objects.create(length=box_serializer.data.get('length'),
                                 width=box_serializer.data.get('width'),
                                 height=box_serializer.data.get('height'),
                                 configuration=box_serializer.data.get('configuration'),
                                 customer_id=box_serializer.data.get('customer_id'))
        box.save()
        return Response(data=BoxSerializer(box).data, status=status.HTTP_201_CREATED)


class AllCustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        customer_serializer = CustomerSerializer(data=request.data)
        customer_serializer.is_valid(raise_exception=True)
        customer = Customer.objects.create(name=customer_serializer.data.get('name'))
        customer.save()
        return Response(data=CustomerSerializer(customer).data, status=status.HTTP_201_CREATED)
