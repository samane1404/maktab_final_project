from itertools import chain
from operator import attrgetter

from django.urls import reverse

from .forms import *
from django.db.models import Q, Sum
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from rest_framework import generics, permissions
from django.views.generic import ListView, DetailView, TemplateView
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
        return JsonResponse(languages, safe=False,)
    else:
        return render(request, 'store/search2.html')


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
    a = Branch.objects.all().filter(menu_sett__orderitem_set__order__status='register').annotate(s=Sum("menu_sett__price"))
    aa = {
        'a': a
    }
    print(aa)
    t = JsonResponse({
                'name': list(a.values_list('name', flat=True))
            })
    return render(req, 'store/best_restaurant.html', aa)


def best_food(x):
    a = Food.objects.all().filter(menu_set__orderitem_set__order__status='registration').annotate(s=Sum("menu_set__quantity"))
    aa = {
        'a': a
    }
    print(aa)
    t = JsonResponse({
                'name': list(a.values_list('name', flat=True))
            })
    return t

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



def merge_dicts(x, y):
    """
    Given two dicts, merge them into a new dict as a shallow copy.
    """
    z = x.copy()
    z.update(y)
    return z
class MultipleFormView(TemplateView):
    """
    View mixin that handles multiple forms / formsets.
    After the successful data is inserted ``self.process_forms`` is called.
    """
    form_classes = {}

    def get_context_data(self, **kwargs):
        context = super(MultipleFormView, self).get_context_data(**kwargs)
        forms_initialized = {name: form(prefix=name)
                             for name, form in self.form_classes.items()}

        return merge_dicts(context, forms_initialized)

    def post(self, request):
        forms_initialized = {
            name: form(prefix=name, data=request.POST)
            for name, form in self.form_classes.items()}

        valid = all([form_class.is_valid()
                     for form_class in forms_initialized.values()])
        if valid:
            return self.process_forms(forms_initialized)
        else:
            context = merge_dicts(self.get_context_data(), forms_initialized)
            return self.render_to_response(context)

    def process_forms(self, form_instances):
        raise NotImplemented


class MultipleFormsDemoView(MultipleFormView):
    template_name = "store/profile_managers.html"
    form_classes = {
        'restaurant_form': RestaurantForm,
        'branch_form': BranchForm,
        'food_form': FoodForm,
        'menu_form': MenuForm,
        'categorymeel_form': CategoryMeelForm,
        'categoryfood_form': CategoryFoodForm,
                    }

    success_urls = {
        'restaurant_form': reverse_lazy('users-home'),
        'branch_form': reverse_lazy('users-home'),
        'food_form': reverse_lazy('users-home'),
        'menu_form': reverse_lazy('users-home'),
        'categorymeel_form': reverse_lazy('users-home'),
        'categoryfood_form': reverse_lazy('users-home'),

    }

    def get_success_url(self):
        return reverse('users-home')

    def forms_valid(self, forms):
        restaurant = forms['restaurant_form'].save(commit=False)
        branch = forms['branch_form'].save(commit=False)
        food = forms['food_form'].save(commit=False)
        menu = forms['menu_form'].save(commit=False)
        categorymeel = forms['categorymeel_form'].save(commit=False)
        categoryfood = forms['categoryfood_form'].save(commit=False)

        return super(MultipleFormsDemoView, self).forms_valid(forms)





