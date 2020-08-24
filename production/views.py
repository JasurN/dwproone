from rest_framework import generics

from production.models import Production
from production.serializers import ProductionSerializer


class ProductionListCreateView(generics.ListCreateAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer


class CorrugatorHistoryListCreateView(generics.ListCreateAPIView):
    pass


class FlexHistoryListCreateView(generics.ListCreateAPIView):
    pass


class ThompsonHistoryListCreateView(generics.ListCreateAPIView):
    pass


class GlueHistoryListCreateView(generics.ListCreateAPIView):
    pass
