from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import *

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}




class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['name', 'city', 'address', 'description', 'main', ]
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['restaurant'] = CategoryFoodSerializer(instance.restaurant_id).data
        return response


class CategoryMeelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMeel
        fields = ['name']

class CategoryFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryFood
        fields = ['name']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['price', 'quantity', 'branch_id']
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['branch'] = BranchSerializer(instance.branch_id).data
        return response

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['status', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class FoodSerializer(serializers.ModelSerializer):
    menu_set = MenuSerializer(many=True)
    category_meel_id = CategoryMeelSerializer(many=True)
    class Meta:
        model = Food
        fields = ['name', 'description', 'image', 'menu_set', 'category_meel_id', 'category_food_id']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category_food'] = CategoryFoodSerializer(instance.category_food_id).data
        return response

class RestaurantSerializer(serializers.ModelSerializer):
    branch_set = BranchSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = ['name', 'branch_set']
