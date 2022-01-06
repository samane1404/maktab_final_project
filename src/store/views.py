from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *
from .permission import *




# Create your views here.
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




# def q1(x):
#     a = Food.objects.all().filter(menu_set__orderitem_set__status='registration')
#     aa = {
#         'a' : a
#     }
#     print(aa)
#     t = JsonResponse({
#                 'name':list(a.values_list('name', flat=True))
#             })
#     return t
def q2(x):
    a = Branch.objects.all().filter(menu_sett__orderitem_set__status='registration')
    aa = {
        'a' : a
    }
    print(aa)
    t = JsonResponse({
                'name':list(a.values_list('name', flat=True))
            })
    return t
def q3(x):
    a = Restaurant.objects.all().filter(branch_set__menu_sett__orderitem_set__status='registration')
    aa = {
        'a' : a
    }
    print(aa)
    t = JsonResponse({
                'name':list(a.values_list('name', flat=True))
            })
    return t




def q1(req):
    a = Food.objects.filter(menu_set__orderitem_set__status='registration')
    if req.method == "GET" and req.is_ajax:
        result = a.all()[0]
        data = {
            'res': result
        }
        print(data)
        return render(req, 'registration/q1.html', data)
