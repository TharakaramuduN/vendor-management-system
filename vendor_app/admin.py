from django.contrib import admin
from .models import Vendor, PurchaseOrder

# Register your models here.

admin.site.register(Vendor)

class PurchaseOrderAdmin(admin.ModelAdmin):
    readonly_fields = ['issue_date']

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)