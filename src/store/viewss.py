from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .permission import *




# Create your views here.
class RestaurantLists(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class BranchLists(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class FoodLists(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class CategoryMeelLists(generics.ListCreateAPIView):
    queryset = CategoryMeel.objects.all()
    serializer_class = CategoryMeelSerializer


class CategoryMeelDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryMeel.objects.all()
    serializer_class = CategoryMeelSerializer


class CategoryFoodLists(generics.ListCreateAPIView):
    queryset = CategoryFood.objects.all()
    serializer_class = CategoryFoodSerializer


class CategoryFoodDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryFood.objects.all()
    serializer_class = CategoryFoodSerializer


class MenuLists(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class OrderItemLists(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderLists(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



