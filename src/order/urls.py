from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('add_to_cart/<slug:slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug:slug>/', remove_from_cart, name='remove_from_cart'),
    path('order_summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('remove_single_item_from_cart/<slug:slug>/', remove_single_item_from_cart,
         name='remove_single_item_from_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('history_orders/', history_orders, name='history_orders'),
    path('orders/', orders, name='orders'),
]
