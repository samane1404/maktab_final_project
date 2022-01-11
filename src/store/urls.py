from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
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


]
