from django.contrib import admin
from .models import *
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))

    image_tag.short_description = 'Product Image Preview'
    readonly_fields = ['image_tag']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

# Register your models here.
