from django.urls import path, include
from .views import *
from .viewss import *


urlpatterns = [
    path('restaurant/', RestaurantList.as_view(), name='restaurant'),
    path('restaurant/<int:pk>', RestaurantDetail.as_view()),
    path('branch/', BranchList.as_view(), name='branch'),
    path('branch/<int:pk>', BranchDetail.as_view()),
    path('food/', FoodList.as_view(), name='food'),
    path('food/<int:pk>', FoodDetail.as_view()),
    path('categorymeel/', CategoryMeelList.as_view(), name='categorymeel'),
    path('categorymeel/<int:pk>', CategoryMeelDetail.as_view()),
    path('categoryfood/', CategoryFoodList.as_view(), name='categoryfood'),
    path('categoryfood/<int:pk>', CategoryFoodDetail.as_view()),
    path('menu/', MenuList.as_view(), name='menu'),
    path('menu/<int:pk>', MenuDetail.as_view()),
    path('orderitem/', OrderItemList.as_view(), name='orderitem'),
    path('orderitem/<int:pk>', OrderItemDetail.as_view()),
    path('order/', OrderList.as_view(), name='order'),
    path('order/<int:pk>', OrderDetail.as_view()),
    path('restaurants/', RestaurantLists.as_view(), name='restaurants'),
    path('restaurants/<int:pk>', RestaurantDetails.as_view()),
    path('branchs/', BranchLists.as_view(), name='branchs'),
    path('branchs/<int:pk>', BranchDetails.as_view()),
    path('foods/', FoodLists.as_view(), name='foods'),
    path('foods/<int:pk>', FoodDetails.as_view()),
    path('categorymeels/', CategoryMeelLists.as_view(), name='categorymeels'),
    path('categorymeels/<int:pk>', CategoryMeelDetails.as_view()),
    path('categoryfoods/', CategoryFoodLists.as_view(), name='categoryfoods'),
    path('categoryfoods/<int:pk>', CategoryFoodDetails.as_view()),
    path('registration/q1.html/', q1, name='q1'),
    path('registration/q2.html/', q2, name='q2'),
    path('registration/q3.html/', q3, name='q3'),
]