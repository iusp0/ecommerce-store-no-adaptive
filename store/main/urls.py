from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='bardStore'),
    path('category/<int:category_id>/', products, name='category'),
    path('category/<int:category_id>/page/<int:page_number>/', products, name='category_paginator'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('products/', products, name='products'),
    path('product/<int:product_id>/', product, name='product'),
]
