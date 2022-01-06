from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class CategoryMeelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMeel
        fields = '__all__'

class CategoryFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryFood
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


from django_jalali.serializers.serializerfield import JDateField, JDateTimeField
from rest_framework.serializers import ModelSerializer

from .models import Bar, BarTime


class JDateFieldSerialializer(ModelSerializer):
    date = JDateField()

    class Meta:
        model = Bar
        exclude = []

class JDateTimeFieldSerializer(ModelSerializer):
    datetime = JDateTimeField()

    class Meta:
        model = BarTime
        exclude = []