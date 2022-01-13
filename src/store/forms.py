from django import forms
from .models import *


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name']


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name']


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description']


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['price', 'quantity', 'image']


class CategoryMeelForm(forms.ModelForm):
    class Meta:
        model = CategoryMeel
        fields = ['name']


class CategoryFoodForm(forms.ModelForm):
    class Meta:
        model = CategoryFood
        fields = ['name']