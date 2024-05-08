from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer

# Create your views here.

class VendorPerformanceListAPIView(RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer