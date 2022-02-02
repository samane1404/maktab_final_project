from django.contrib import messages
from django.db.models import Q, Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import *


class Home(ListView):
    paginate_by = 5
    template_name = 'home.html'


class MenuDetail(DetailView):
    model = Menu
    template_name = 'restaurant/details_menu.html'



def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request is updated successfully')
            return redirect(create_restaurant)
    else:
        form = RestaurantForm()
    re = Restaurant.objects.all()
    return render(request, 'restaurant/create_restaurant.html', {'form': form, 'restaurant_list': re})


def edit_restaurant(request, pk=None):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request is updated successfully')
            return redirect('create_restaurant')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurant/edit_restaurant.html', {'form': form, 'restaurant': restaurant})


def delete_restaurant(request, pk=None):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantDeleteForm(request.POST, instance=restaurant)
        if form.is_valid():
            restaurant.delete()
            messages.success(request, 'Your request is updated successfully')
            return redirect('create_restaurant')
    else:
        form = RestaurantDeleteForm(instance=restaurant)
    return render(request, 'restaurant/delete_restaurant.html', {'form': form, 'restaurant': restaurant})


def create_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request is updated successfully')
            return redirect(create_branch)
    else:
        form = BranchForm()
    re = Branch.objects.all()
    return render(request, 'restaurant/create_branch.html', {'form': form, 'branch_list': re})


def edit_branch(request, pk=None):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request is updated successfully')
            return redirect('create_branch')
    else:
        form = BranchForm(instance=branch)
    return render(request, 'restaurant/edit_branch.html', {'form': form, 'branch': branch})


def delete_branch(request, pk=None):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == 'POST':
        form = BranchDeleteForm(request.POST, instance=branch)
        if form.is_valid():
            branch.delete()
            messages.success(request, 'Your request is updated successfully')
            return redirect('create_branch')
    else:
        form = BranchDeleteForm(instance=branch)
    return render(request, 'restaurant/delete_branch.html', {'form': form, 'branch': branch})


def create_category_food(request):
    if request.method == 'POST':
        form = CategoryFoodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request is updated successfully')
            return redirect(create_category_food)
    else:
        form = CategoryFoodForm()
    re = CategoryFood.objects.all()
    return render(request, 'restaurant/create_category_food.html', {'form': form, 'category_food_list': re})


def edit_category_food(request, pk=None):
    category_food = get_object_or_404(CategoryFood, pk=pk)
    if request.method == 'POST':
        form = CategoryFoodForm(request.POST, instance=category_food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request is updated successfully')
            return redirect('create_category_food')
    else:
        form = CategoryFoodForm(instance=category_food)
    return render(request, 'restaurant/edit_category_food.html', {'form': form, 'category_food': category_food})


def delete_category_food(request, pk=None):
    category_food = get_object_or_404(CategoryFood, pk=pk)
    if request.method == 'POST':
        form = CategoryFoodDeleteForm(request.POST, instance=category_food)
        if form.is_valid():
            category_food.delete()
            messages.success(request, 'Your request is updated successfully')
            return redirect('create_category_food')
    else:
        form = CategoryFoodDeleteForm(instance=category_food)
    return render(request, 'restaurant/delete_category_food.html', {'form': form, 'category_food': category_food})


def create_category_meel(request):
    if request.method == 'POST':
        form = CategoryMeelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request is updated successfully')
            return redirect(create_category_meel)
    else:
        form = CategoryMeelForm()
    re = CategoryMeel.objects.all()
    return render(request, 'restaurant/create_category_meel.html', {'form': form, 'category_meel_list': re})


def edit_category_meel(request, pk=None):
    category_meel = get_object_or_404(CategoryMeel, pk=pk)
    if request.method == 'POST':
        form = CategoryMeelForm(request.POST, instance=category_meel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request is updated successfully')
            return redirect('create_category_meel')
    else:
        form = CategoryMeelForm(instance=category_meel)
    return render(request, 'restaurant/edit_category_meel.html', {'form': form, 'category_meel': category_meel})


def delete_category_meel(request, pk=None):
    category_meel = get_object_or_404(CategoryMeel, pk=pk)
    if request.method == 'POST':
        form = CategoryMeelDeleteForm(request.POST, instance=category_meel)
        if form.is_valid():
            category_meel.delete()
            messages.success(request, 'Your request is updated successfully')
            return redirect('create_category_meel')
    else:
        form = CategoryMeelDeleteForm(instance=category_meel)
    return render(request, 'restaurant/delete_category_meel.html', {'form': form, 'category_meel': category_meel})


def create_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request is updated successfully')
            return redirect(create_food)
    else:
        form = FoodForm()
    re = Food.objects.all()
    return render(request, 'restaurant/create_food.html', {'form': form, 'food_list': re})


def edit_food(request, pk=None):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request is updated successfully')
            return redirect('create_food')
    else:
        form = FoodForm(instance=food)
    return render(request, 'restaurant/edit_food.html', {'form': form, 'food': food})


def delete_food(request, pk=None):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        form = FoodDeleteForm(request.POST, instance=food)
        if form.is_valid():
            food.delete()
            messages.success(request, 'Your request is updated successfully')
            return redirect('create_food')
    else:
        form = FoodDeleteForm(instance=food)
    return render(request, 'restaurant/delete_food.html', {'form': form, 'food': food})


def create_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # img_obj = form.instance
            messages.success(request, 'Your request is updated successfully')
            return redirect(create_menu)
    else:
        form = MenuForm()
    re = Menu.objects.all()
    return render(request, 'restaurant/create_menu.html', {'form': form, 'menu_list': re})


def edit_menu(request, pk=None):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request is updated successfully')
            return redirect('create_menu')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'restaurant/edit_menu.html', {'form': form, 'menu': menu})


def delete_menu(request, pk=None):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuDeleteForm(request.POST, instance=menu)
        if form.is_valid():
            menu.delete()
            messages.success(request, 'Your request is updated successfully')
            return redirect('create_menu')
    else:
        form = MenuDeleteForm(instance=menu)
    return render(request, 'restaurant/delete_menu.html', {'form': form, 'menu': menu})


def menu_manager(request):
    re = Menu.objects.filter(branch__manager=request.user)
    context = {
        'object_list': re,
    }
    return render(request, 'restaurant/menu_manager.html', context)


def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        results = Menu.objects.filter(Q(food__name__icontains=query) | Q(branch__name__icontains=query)
                                      | Q(branch__restaurant__name__icontains=query)
                                      | Q(food__category_food__name__icontains=query))
    return render(request, 'restaurant/search.html', {'query': query, 'results': results})


def best_food(request):
    a = Menu.objects.all().filter(order_item_order__ordered=True).annotate(s=Sum("quantity"))[:3]
    aa = {
        'aaa': a
    }
    return render(request, 'restaurant/best_food.html', aa)



