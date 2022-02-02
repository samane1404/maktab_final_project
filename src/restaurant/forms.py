from .models import *
from django.forms import ModelForm
from django import forms


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantDeleteForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = []


class BranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'


class BranchDeleteForm(ModelForm):
    class Meta:
        model = Branch
        fields = []


class CategoryFoodForm(ModelForm):
    class Meta:
        model = CategoryFood
        fields = '__all__'


class CategoryFoodDeleteForm(ModelForm):
    class Meta:
        model = CategoryFood
        fields = []


class CategoryMeelForm(ModelForm):
    class Meta:
        model = CategoryMeel
        fields = '__all__'


class CategoryMeelDeleteForm(ModelForm):
    class Meta:
        model = CategoryMeel
        fields = []


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class FoodDeleteForm(ModelForm):
    class Meta:
        model = Food
        fields = []


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'


class MenuDeleteForm(ModelForm):
    class Meta:
        model = Menu
        fields = []