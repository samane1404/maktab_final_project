from django import forms
from django.forms import formset_factory, ModelForm

from .models import *

# # class forms.ModelForm(forms.Form):
# #     action = forms.CharField(max_length=60, widget=forms.HiddenInput())
#
#
# class MenuForm(forms.ModelForm):
#     price = forms.IntegerField()
#     quantity = forms.IntegerField()
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
#     class Meta:
#         model = Menu
#         fields = ['price', 'quantity', 'image']
# MenuFormset = formset_factory(MenuForm, extra=1)
#
#
# class FoodForm(forms.ModelForm):
#     name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'name',
#                                                               'class': 'form-control',
#                                                               }))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
#     class Meta:
#         model = Food
#         fields = ['name', 'description']
# FoodFormset = formset_factory(FoodForm, extra=1)
#
#
# class BranchForm(forms.ModelForm):
#     name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'name',
#                                                               'class': 'form-control',
#                                                               }))
#     main = forms.BooleanField()
#     class Meta:
#         model = Branch
#         fields = ['name', 'main']
# BranchFormset = formset_factory(BranchForm, extra=1)
#
#
# class RestaurantForm(forms.ModelForm):
#     name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'name',
#                                                               'class': 'form-control',
#                                                               }))
#     class Meta:
#         model = Restaurant
#         fields = ['name']
# RestaurantFormset = formset_factory(RestaurantForm, extra=1)
#
#
# class CategoryMeelForm(forms.ModelForm):
#     name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'name',
#                                                               'class': 'form-control',
#                                                               }))
#     class Meta:
#         model = CategoryMeel
#         fields = ['name']
# CategoryMeelFormset = formset_factory(CategoryMeelForm, extra=1)
#
#
# class CategoryFoodForm(forms.ModelForm):
#     name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'name',
#                                                               'class': 'form-control',
#                                                               }))
#     class Meta:
#         model = CategoryFood
#         fields = ['name']
# CategoryFoodFormset = formset_factory(CategoryFoodForm, extra=1)



class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

class CategoeyForm1(ModelForm):
    class Meta:
        model = CategoryMeel
        fields = '__all__'

class CategoeyForm2(ModelForm):
    class Meta:
        model = CategoryFood
        fields = '__all__'

class BranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = '__all__'

class MenuDeleteForm(ModelForm):
    class Meta:
        model = Menu
        fields = []

class RestDeleteForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = []

class BranchDeleteForm(ModelForm):
    class Meta:
        model = Branch
        fields = []

class FoodDeleteForm(ModelForm):
    class Meta:
        model = Food
        fields = []

class CatMeelDeleteForm(ModelForm):
    class Meta:
        model = CategoryMeel
        fields = []

class CatFoodDeleteForm(ModelForm):
    class Meta:
        model = CategoryFood
        fields = []
