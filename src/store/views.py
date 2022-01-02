from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *




# Create your views here.
class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class BranchList(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetail(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class FoodList(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetail(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class CategoryMeelList(generics.ListAPIView):
    queryset = CategoryMeel.objects.all()
    serializer_class = CategoryMeelSerializer

class CategoryMeelDetail(generics.RetrieveAPIView):
    queryset = CategoryMeel.objects.all()
    serializer_class = CategoryMeelSerializer

class CategoryFoodList(generics.ListAPIView):
    queryset = CategoryFood.objects.all()
    serializer_class = CategoryFoodSerializer

class CategoryFoodDetail(generics.RetrieveAPIView):
    queryset = CategoryFood.objects.all()
    serializer_class = CategoryFoodSerializer

class MenuList(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetail(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OrderItemList(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(generics.RetrieveAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


