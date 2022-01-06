from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
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