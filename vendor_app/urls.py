from django.urls import path
from .views import VendorListCreateAPIView, VendorRetrieveUpdateDestroyAPIView, PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView, AcknowledgmentDateUpdateAPIView

urlpatterns = [
    path('vendors/', VendorListCreateAPIView.as_view(), name='vendors-list'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-details'),
    path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase_orders-list'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase_order_details'),
    path('purchase_orders/<int:pk>/acknowledge/',AcknowledgmentDateUpdateAPIView.as_view(), name='update-acknowledge-date')
]