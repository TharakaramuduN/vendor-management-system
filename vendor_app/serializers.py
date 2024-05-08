from .models import Vendor, PurchaseOrder
from rest_framework import serializers
import uuid
from django.utils import timezone

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ['vendor_code','quality_rating_avg','average_response_time','fulfillment_rate','on_time_delivery_rate']
    
    def create(self, validated_data):
        validated_data['vendor_code'] = uuid.uuid4()
        return super().create(validated_data)

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        read_only_fields = ['po_number']
    
    def create(self, validated_data):
        validated_data['po_number'] = uuid.uuid4()
        return super().create(validated_data)