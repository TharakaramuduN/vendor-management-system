from django.urls import path
from .views import VendorPerformanceListAPIView

urlpatterns = [
    path('vendors/<int:pk>/performance/',VendorPerformanceListAPIView.as_view(), name='vendor-performance')
]
