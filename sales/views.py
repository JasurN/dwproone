from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from sales.models import Order, Box, Customer, Contract
from sales.serializers import OrdersSerializer, BoxSerializer, CustomerSerializer, AddBoxSerializer, ContractSerializer, \
    AddOrderSerializer


class OrdersListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer

    def create(self, request, *args, **kwargs):
        order_serializer = AddOrderSerializer(data=request.data)
        order_serializer.is_valid(raise_exception=True)
        order = Order.objects.create(contract_id=order_serializer.data.get('contract_id'),
                                     box_id=order_serializer.data.get('box_id'),
                                     order_date=order_serializer.data.get('order_date'),
                                     ship_date=order_serializer.data.get('ship_date'),
                                     quantity=order_serializer.data.get('quantity'),
                                     remaining=order_serializer.data.get('quantity'),
                                     delivered=0)
        order.save()
        return Response(data=OrdersSerializer(order).data, status=status.HTTP_201_CREATED)


class OrderDetailView(APIView):
    serializer_class = OrdersSerializer

    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        order_serializer = OrdersSerializer(order)
        return Response(status=status.HTTP_200_OK,
                        data=order_serializer.data)

    def patch(self, request, pk):
        order_serializer = OrdersSerializer(data=request.data)
        order_serializer.is_valid(raise_exception=True)
        order = Order.objects.get(pk=pk)
        if request.data.get('delivered_amount') > order.remaining:
            return Response(data={'message': 'delivered amount is more than remaining'},
                            status=status.HTTP_400_BAD_REQUEST)
        order.remaining = order.remaining - request.data.get('delivered_amount')
        order.delivered = order.delivered + request.data.get('delivered_amount')
        order.save()
        return Response(data=OrdersSerializer(order).data,
                        status=status.HTTP_200_OK)


class BoxListView(generics.ListCreateAPIView):
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


class BoxDetailView(APIView):
    serializer_class = BoxSerializer

    def get(self, request, pk):
        box = Box.objects.get(pk=pk)
        box_serializer = BoxSerializer(box)
        return Response(status=status.HTTP_200_OK,
                        data=box_serializer.data)


class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        customer_serializer = CustomerSerializer(data=request.data)
        customer_serializer.is_valid(raise_exception=True)
        customer = Customer.objects.create(name=customer_serializer.data.get('name'))
        customer.save()
        return Response(data=CustomerSerializer(customer).data, status=status.HTTP_201_CREATED)


class CustomerDetailView(APIView):
    serializer_class = CustomerSerializer

    def get(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        customer_serializer = CustomerSerializer(customer)
        return Response(status=status.HTTP_200_OK,
                        data=customer_serializer.data)


class ContractListView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_201_CREATED)


class ContractDetailView(APIView):
    serializer_class = CustomerSerializer

    def get(self, request, pk):
        contract = Contract.objects.get(pk=pk)
        contract = ContractSerializer(contract)
        return Response(status=status.HTTP_200_OK,
                        data=contract.data)
