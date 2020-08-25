from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from sales.filters import OrderDeliveryFilter, OrderFilter, BoxFilter
from sales.models import Order, Box, Customer, Contract, OrderDelivery
from sales.serializers import OrderSerializer, BoxSerializer, CustomerSerializer, AddBoxSerializer, ContractSerializer, \
    AddOrderSerializer, OrderDeliverySerializer


class OrdersListView(generics.ListCreateAPIView):
    queryset = Order.objects.filter(remaining__gt=0)
    serializer_class = OrderSerializer
    filterset_class = OrderFilter

    def create(self, request, *args, **kwargs):
        order_serializer = AddOrderSerializer(data=request.data)
        order_serializer.is_valid(raise_exception=True)
        order = Order.objects.create(contract_id=order_serializer.data.get('contract_id'),
                                     box_id=order_serializer.data.get('box_id'),
                                     order_date=order_serializer.data.get('order_date'),
                                     ship_date=order_serializer.data.get('ship_date'),
                                     quantity=order_serializer.data.get('quantity'),
                                     remaining=order_serializer.data.get('quantity'),
                                     flex=request.data.get('flex', False),
                                     thompson=request.data.get('thompson', False),
                                     glue=request.data.get('glue', False),
                                     stitching=request.data.get('stitching', False),
                                     delivered=0)
        order.save()
        return Response(data=OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class OrderDetailView(APIView):
    serializer_class = OrderSerializer
    filterset_class = OrderFilter

    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        order_serializer = OrderSerializer(order)
        return Response(status=status.HTTP_200_OK,
                        data=order_serializer.data)

    def patch(self, request, pk):
        order_serializer = OrderSerializer(data=request.data)
        order_serializer.is_valid(raise_exception=True)
        order = Order.objects.get(pk=pk)
        if request.data.get('delivered_amount') > order.remaining:
            return Response(data={'message': 'delivered amount is more than remaining'},
                            status=status.HTTP_400_BAD_REQUEST)
        order.remaining = order.remaining - request.data.get('delivered_amount')
        order.delivered = order.delivered + request.data.get('delivered_amount')
        OrderDelivery.objects.create(order=order,
                                     amount=request.data.get('delivered_amount'))
        order.save()
        return Response(data=OrderSerializer(order).data,
                        status=status.HTTP_200_OK)


class BoxListCreateView(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    filterset_class = BoxFilter

    def create(self, request, *args, **kwargs):
        box_serializer = AddBoxSerializer(data=request.data)
        box_serializer.is_valid(raise_exception=True)
        dimension = f"{box_serializer.data.get('length')}x" \
                    f"{box_serializer.data.get('width')}x{box_serializer.data.get('height')}"
        box = Box.objects.create(length=box_serializer.data.get('length'),
                                 width=box_serializer.data.get('width'),
                                 height=box_serializer.data.get('height'),
                                 configuration=box_serializer.data.get('configuration'),
                                 customer_id=box_serializer.data.get('customer_id'),
                                 dimension=dimension)
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


class ContractListCreateView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def create(self, request, *args, **kwargs):
        contract_serializer = ContractSerializer(data=request.data)
        contract_serializer.is_valid(raise_exception=True)
        contract = Contract.objects.create(customer_id=request.data.get('customer_id'),
                                           contract_number=request.data.get('contract_number'))
        contract.save()
        return Response(data=ContractSerializer(contract).data, status=status.HTTP_201_CREATED)


class ContractDetailView(APIView):
    serializer_class = CustomerSerializer

    def get(self, request, pk):
        contract = Contract.objects.get(pk=pk)
        contract = ContractSerializer(contract)
        return Response(status=status.HTTP_200_OK,
                        data=contract.data)


class OrderDeliveryListView(generics.ListAPIView):
    queryset = OrderDelivery.objects.all()
    serializer_class = OrderDeliverySerializer
    filterset_class = OrderDeliveryFilter
