from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .permission import *




# Create your views here.
class RestaurantLists(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetails(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class BranchLists(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetails(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class FoodLists(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetails(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class CategoryMeelLists(generics.ListAPIView):
    queryset = CategoryMeel.objects.all()
    serializer_class = CategoryMeelSerializer


class CategoryMeelDetails(generics.RetrieveAPIView):
    queryset = CategoryMeel.objects.all()
    serializer_class = CategoryMeelSerializer


class CategoryFoodLists(generics.ListAPIView):
    queryset = CategoryFood.objects.all()
    serializer_class = CategoryFoodSerializer


class CategoryFoodDetails(generics.RetrieveAPIView):
    queryset = CategoryFood.objects.all()
    serializer_class = CategoryFoodSerializer


class MenuLists(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetails(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

import jdatetime
gregorian_date = jdatetime.date(1396,2,30).togregorian()
jalili_date =  jdatetime.date.fromgregorian(day=19,month=5,year=2017)



