from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', user_profile, name='user_profile'),
    path('orders/', user_orders, name='user_orders'),
    path('favorites/', user_favorites, name='user_favorites'),
    path('change_password/', user_password, name='user_password'),
    path('cart/', cart, name='cart'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
