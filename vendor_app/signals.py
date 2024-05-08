from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PurchaseOrder
from django.utils import timezone
from vendor_performance.utils import update_average_response_time,update_fulfillment_rate,update_on_time_delivery_rate,update_quality_rating_avg
from vendor_performance.models import HistoricalPerformance
from django.db.models import Avg, F

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_metrics(sender, instance, created, **kwargs):

    if instance.tracker.has_changed('status') and instance.status == 'completed':
        vendor = instance.vendor
        update_on_time_delivery_rate(vendor)
        update_fulfillment_rate(vendor)
    
    if instance.tracker.has_changed('quality_rating') and instance.status == 'completed':
        vendor = instance.vendor
        update_quality_rating_avg(vendor)
    
    if instance.tracker.has_changed('acknowledgment_date'):
        vendor = instance.vendor
        update_average_response_time(vendor)
    
    if instance.tracker.changed():
        vendor = instance.vendor
        HistoricalPerformance.objects.create(
            vendor = vendor,
            on_time_delivery_rate = vendor.on_time_delivery_rate,
            quality_rating_avg = vendor.quality_rating_avg,
            average_response_time = vendor.average_response_time,
            fulfillment_rate = vendor.fulfillment_rate
        )
        

@receiver(post_delete, sender=PurchaseOrder)
def update_vendor_performance_metrics_on_delete(sender, instance, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        update_on_time_delivery_rate(vendor)
        update_quality_rating_avg(vendor)
        update_fulfillment_rate(vendor)