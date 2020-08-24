from rest_framework import generics, status
from rest_framework.response import Response

from production.models import Production
from production.serializers import ProductionSerializer, AddProductionSerializer


class ProductionListCreateView(generics.ListCreateAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer

    def create(self, request, *args, **kwargs):
        production_serializer = AddProductionSerializer(data=request.data)
        production_serializer.is_valid(raise_exception=True)
        production = Production.objects.create(order_id=production_serializer.data.get('order_id'),
                                               scheduled_date=production_serializer.data.get('scheduled_date'),
                                               production_order=production_serializer.data.get('production_order'))
        return Response(data=ProductionSerializer(production).data, status=status.HTTP_201_CREATED)


class CorrugatorHistoryListCreateView(generics.ListCreateAPIView):
    pass


class FlexHistoryListCreateView(generics.ListCreateAPIView):
    pass


class ThompsonHistoryListCreateView(generics.ListCreateAPIView):
    pass


class GlueHistoryListCreateView(generics.ListCreateAPIView):
    pass
