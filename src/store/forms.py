from django import forms
from .models import *

class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())


class MenuForm(MultipleForm):
    price = forms.IntegerField()
    quantity = forms.IntegerField()
    image = forms.ImageField()
    created_time = forms.DateField()
    class Meta:
        model = Menu
        fields = ['price', 'quantity', 'image', 'created_time']


class FoodForm(MultipleForm):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300)
    class Meta:
        model = Food
        fields = ['name', 'description']


class BranchForm(MultipleForm):
    name = forms.CharField(max_length=50)
    main = forms.BooleanField()
    class Meta:
        model = Branch
        fields = ['name', 'main']


class RestaurantForm(MultipleForm):
    name = forms.CharField(max_length=50)
    class Meta:
        model = Restaurant
        fields = ['name']


class CategoryMeelForm(MultipleForm):
    name = forms.CharField(max_length=50)
    class Meta:
        model = CategoryMeel
        fields = ['name']


class CategoryFoodForm(MultipleForm):
    name = forms.CharField(max_length=50)
    class Meta:
        model = CategoryFood
        fields = ['name']
