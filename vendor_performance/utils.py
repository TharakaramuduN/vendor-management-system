from django.utils import timezone
from django.db.models import Avg,F
from vendor_app.models import PurchaseOrder

def update_on_time_delivery_rate(vendor):
    completed_orders = PurchaseOrder.objects.filter(status='completed', vendor = vendor)
    on_time_deliveries_count = completed_orders.filter(delivery_date__lte = F('expected_delivery_date') ).count()
    on_time_delivery_rate = (on_time_deliveries_count / completed_orders.count()) * 100 if completed_orders.count() else 0
    vendor.on_time_delivery_rate = on_time_delivery_rate
    print(on_time_delivery_rate)
    vendor.save()
    

def update_quality_rating_avg(vendor):
    completed_orders = PurchaseOrder.objects.filter(status='completed', vendor=vendor)
    quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0
    vendor.quality_rating_avg = quality_rating_avg
    vendor.save()

def update_average_response_time(vendor):
    completed_orders = PurchaseOrder.objects.filter(status='completed',vendor=vendor)
    response_times = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull = False).annotate(
        response_time = F('acknowledgment_date') - F('issue_date')).values_list('response_time', flat=True)
    avg_response_timedelta = sum(response_times,timezone.timedelta()) / response_times.count() if response_times else 0
    avg_response_time = avg_response_timedelta.total_seconds()
    vendor.average_response_time = avg_response_time
    vendor.save()

def update_fulfillment_rate(vendor):
    completed_orders = PurchaseOrder.objects.filter(status='completed',vendor=vendor)
    fulfilled_orders_count = completed_orders.filter(quality_rating__gte = 3, quality_rating__isnull = True).count()
    fulfillment_rate = (fulfilled_orders_count / completed_orders.count()) * 100 if completed_orders else 0
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()