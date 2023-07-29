from django.contrib import admin
from .models import Product, ProductCategory, Basket


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'size', 'quantity', 'category']
    fields = ['name', 'description', ('price', 'discount', 'quantity',), 'size', 'image_1', 'image_2', 'image_3', 'category']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    fields = ['name', 'description']

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity']
    extra = 0