from django.contrib import admin
from .models import *
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))

    image_tag.short_description = 'Product Image Preview'
    readonly_fields = ['image_tag']

class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    readonly_fields = ('product', 'quantity', 'item_total_price')
    extra = 0

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'purchased_at', 'total_price') 
    inlines = [PurchaseItemInline] 






admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Purchase, PurchaseAdmin)

# Register your models here.
