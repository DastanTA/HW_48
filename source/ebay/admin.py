from django.contrib import admin
from ebay.models import Product


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'remainder', 'price']
    list_filter = ['category']
    search_fields = ['name']
    readonly_fields = []
    exclude = []


admin.site.register(Product, ProductsAdmin)
