from itertools import chain
from operator import attrgetter

from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, permissions
from django.views.generic import ListView, DetailView
from .serializers import *


def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        results = Menu.objects.filter(Q(food__name__icontains=query) | Q(quantity__icontains=query)
                                    | Q(price__icontains=query) | Q(branch__name__icontains=query)
                                    | Q(branch__restaurant__name__icontains=query)
                                    | Q(food__category_food__name__icontains=query)
                                    | Q(food__category_meel__name__icontains=query))
    return render(request, 'store/search.html', {'query': query, 'results': results})


def list(req):
    re = Menu.objects.all()
    p = Food.objects.all()
    b = Branch.objects.all()
    context ={
        'object_list':re,
        'menu_set':p,
        'menu_sett':b,
    }
    return render(req, 'home.html', context)


def list_restaurant(req):
    b = Restaurant.objects.all()
    re = Branch.objects.all()
    context = {
        'object_list': re,
        'menu_sett': b,
    }
    return render(req, 'store/list_restaurant.html', context)


def list_food(req):
    me = Food.objects.all()
    ce = CategoryFood.objects.all()
    be = Branch.objects.all()
    re = Menu.objects.all()
    context = {
        'object_list': re,
        'food_set': ce,
        'branch_set1': be,
        'menu_set': me,
    }
    return render(req, 'store/list_food.html', context)


def best_restaurant(req):
    re = Food.objects.all()
    context = {
        'object_list': re,
    }
    return render(req, 'store/best_restaurant.html', context)


def best_food(req):
    re = Food.objects.all()
    context = {
        'object_list': re,
    }
    return render(req, 'store/best_food.html', context)


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_desrtoy(self, serializer):
        serializer.save(owner=self.request.user)


class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_desrtoy(self, serializer):
        serializer.save(owner=self.request.user)


class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_desrtoy(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryMeelList(generics.ListCreateAPIView):
    queryset = CategoryMeel.objects.all()
    serializer_class = CategoryMeelSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryMeelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryMeel.objects.all()
    serializer_class = CategoryMeelSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_desrtoy(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryFoodList(generics.ListCreateAPIView):
    queryset = CategoryFood.objects.all()
    serializer_class = CategoryFoodSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryFoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryFood.objects.all()
    serializer_class = CategoryFoodSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_desrtoy(self, serializer):
        serializer.save(owner=self.request.user)


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_desrtoy(self, serializer):
        serializer.save(owner=self.request.user)


class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_desrtoy(self, serializer):
        serializer.save(owner=self.request.user)


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_desrtoy(self, serializer):
        serializer.save(owner=self.request.user)

#-------------------------------------------------------------------------------

