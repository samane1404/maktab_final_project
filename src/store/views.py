from django.contrib import messages
from django.views.generic import DetailView

from .forms import *
from django.db.models import Q, Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics, permissions
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


def search2(request):
    if request.GET and request.is_ajax():
        q = request.GET.get('term')
        print(q)
        student_object = Food.objects.filter(name__icontains=q)
        languages = []
        for r in student_object:
            languages.append(r.name)
            print(languages)
        return JsonResponse(languages, safe=False, )
    else:
        return render(request, 'store/search2.html')


def list(req):
    re = Menu.objects.all()
    p = Food.objects.all()
    b = Branch.objects.all()
    context = {
        'object_list': re,
        'menu_set': p,
        'menu_sett': b,
    }
    return render(req, 'home.html', context)

class details(DetailView):
    model = Menu
    template_name = "store/details.html"


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
    a = Branch.objects.all().filter(menu_sett__orderitem_set__order__status='registration').annotate(s=Sum("menu_sett__quantity"))[:3]
    aa = {
        'aaa': a
    }
    return render(req, 'store/best_restaurant.html', aa)


def best_food(x):
    a = Menu.objects.all().filter(orderitem_set__order__status='registration').annotate(s=Sum("quantity"))[:3]
    aa = {
        'aaa': a
    }
    return render(x, 'store/best_food.html', aa)


def orders(x):
    a = Menu.objects.all().filter(orderitem_set__order__status='registration')
    aa = {
        'aaa': a
    }
    return render(x, 'store/orders.html', aa)


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


def search21(request):
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
    return render(request, 'store/seareh2.html', {'query': query, 'results': results})


def rest_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rest_create')
    else:
        form = RestaurantForm()
    return render(request,
                  'store/rest_create.html',
                  {
                      'form': form
                  })

def rest_edit(request, pk=None):
    blog = get_object_or_404(Restaurant, pk=pk)
    if request.method == "POST":
        form = RestaurantForm(request.POST,
                              instance=blog)
        if form.is_valid():
            form.save()
            return redirect('list_rest')
    else:
        form = RestaurantForm(instance=blog)

    return render(request,
                  'store/rest_edit.html',
                  {
                      'form': form,
                      'blog': blog
                  })


def rest_del(request, pk=None):
    blog = get_object_or_404(Restaurant, pk=pk)
    if request.method == "POST":
        form = RestDeleteForm(request.POST,
                                    instance=blog)
        if form.is_valid():
            blog.delete()
            return redirect('list_menu')
    else:
        form = RestDeleteForm(instance=blog)

    return render(request, 'store/rest_del.html',
                  {
                      'form': form,
                      'blog': blog,
                  })



def category1_create(request):
    if request.method == 'POST':
        form = CategoeyForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category1_create')
    else:
        form = CategoeyForm1()
    return render(request,
                  'store/category1_create.html',
                  {
                      'form': form
                  })

def cat1_edit(request, pk=None):
    blog = get_object_or_404(CategoryMeel, pk=pk)
    if request.method == "POST":
        form = CategoeyForm1(request.POST,
                              instance=blog)
        if form.is_valid():
            form.save()
            return redirect('list_meel')
    else:
        form = CategoeyForm1(instance=blog)

    return render(request,
                  'store/cat1_edit.html',
                  {
                      'form': form,
                      'blog': blog
                  })


def cat1_del(request, pk=None):
    blog = get_object_or_404(CategoryMeel, pk=pk)
    if request.method == "POST":
        form = CatMeelDeleteForm(request.POST,
                                    instance=blog)
        if form.is_valid():
            blog.delete()
            return redirect('list_meel')
    else:
        form = CatMeelDeleteForm(instance=blog)

    return render(request, 'store/cat1_del.html',
                  {
                      'form': form,
                      'blog': blog,
                  })



def category2_create(request):
    if request.method == 'POST':
        form = CategoeyForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category2_create')
    else:
        form = CategoeyForm2()
    return render(request,
                  'store/category2_create.html',
                  {
                      'form': form
                  })

def cat2_edit(request, pk=None):
    blog = get_object_or_404(CategoryFood, pk=pk)
    if request.method == "POST":
        form = CategoeyForm2(request.POST,
                              instance=blog)
        if form.is_valid():
            form.save()
            return redirect('list_foods')
    else:
        form = CategoeyForm2(instance=blog)

    return render(request,
                  'store/cat2_edit.html',
                  {
                      'form': form,
                      'blog': blog
                  })


def cat2_del(request, pk=None):
    blog = get_object_or_404(CategoryFood, pk=pk)
    if request.method == "POST":
        form = CatFoodDeleteForm(request.POST,
                                    instance=blog)
        if form.is_valid():
            blog.delete()
            return redirect('list_foods')
    else:
        form = CatFoodDeleteForm(instance=blog)

    return render(request, 'store/cat2_del.html',
                  {
                      'form': form,
                      'blog': blog,
                  })



def branch_create(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_create')
    else:
        form = BranchForm()
    return render(request,
                  'store/branch_create.html',
                  {
                      'form': form
                  })

def branch_edit(request, pk=None):
    blog = get_object_or_404(Branch, pk=pk)
    if request.method == "POST":
        form = BranchForm(request.POST,
                              instance=blog)
        if form.is_valid():
            form.save()
            return redirect('list_branch')
    else:
        form = BranchForm(instance=blog)

    return render(request,
                  'store/branch_edit.html',
                  {
                      'form': form,
                      'blog': blog
                  })


def branch_del(request, pk=None):
    blog = get_object_or_404(Branch, pk=pk)
    if request.method == "POST":
        form = BranchDeleteForm(request.POST,
                                    instance=blog)
        if form.is_valid():
            blog.delete()
            return redirect('list_branch')
    else:
        form = BranchDeleteForm(instance=blog)

    return render(request, 'store/branch_del.html',
                  {
                      'form': form,
                      'blog': blog,
                  })



def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_create')
    else:
        form = MenuForm()
    return render(request,
                  'store/menu_create.html',
                  {
                      'form': form
                  })

def menu_edit(request, pk=None):
    blog = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        form = MenuForm(request.POST,
                              instance=blog)
        if form.is_valid():
            form.save()
            return redirect('list_menu')
    else:
        form = MenuForm(instance=blog)

    return render(request,
                  'store/menu_edit.html',
                  {
                      'form': form,
                      'blog': blog
                  })


def menu_del(request, pk=None):
    blog = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        form = MenuDeleteForm(request.POST,
                                    instance=blog)
        if form.is_valid():
            blog.delete()
            return redirect('list_menu')
    else:
        form = MenuDeleteForm(instance=blog)

    return render(request, 'store/menu_del.html',
                  {
                      'form': form,
                      'blog': blog,
                  })



def food_create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_create')
    else:
        form = FoodForm()
    return render(request,
                  'store/food_create.html',
                  {
                      'form': form
                  })

def food_edit(request, pk=None):
    blog = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        form = FoodForm(request.POST,
                              instance=blog)
        if form.is_valid():
            form.save()
            return redirect('list_foodss')
    else:
        form = FoodForm(instance=blog)

    return render(request,
                  'store/food_edit.html',
                  {
                      'form': form,
                      'blog': blog
                  })


def food_del(request, pk=None):
    blog = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        form = FoodDeleteForm(request.POST,
                                    instance=blog)
        if form.is_valid():
            blog.delete()
            return redirect('list_foodss')
    else:
        form = FoodDeleteForm(instance=blog)

    return render(request, 'store/food_del.html',
                  {
                      'form': form,
                      'blog': blog,
                  })



def list_rest(request):
    context = {"customer": Restaurant.objects.all()}
    return render(request, "store/list_rest.html", context)


def list_branch(request):
    context = {"customer": Branch.objects.all()}
    return render(request, "store/list_branch.html", context)


def list_meel(request):
    context = {"customer": CategoryMeel.objects.all()}
    return render(request, "store/list_meel.html", context)


def list_foods(request):
    context = {"customer": CategoryFood.objects.all()}
    return render(request, "store/list_foods.html", context)


def list_foodss(request):
    context = {"customer": Food.objects.all()}
    return render(request, "store/list_foodss.html", context)


def list_menu(request):
    context = {"customer": Menu.objects.all()}
    return render(request, "store/list_menu.html", context)


def list_view(request):
    context = {"dataset": Menu.objects.all()}
    return render(request, "store/sss.html", context)


# def orderpage(request):
#     customer = request.session.get('customer')
#     order = Order.get_order_by_customer(customer)
#     print(order)
#     return render(request, 'store/order.html', {'order': order})

