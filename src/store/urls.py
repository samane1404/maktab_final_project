from django.urls import path, include
from .views import *


urlpatterns = [
    path('restaurant/', RestaurantList.as_view()),
    path('restaurant/<int:pk>', RestaurantDetail.as_view()),
    path('branch/', BranchList.as_view()),
    path('branch/<int:pk>', BranchDetail.as_view()),
    path('food/', FoodList.as_view()),
    path('food/<int:pk>', FoodDetail.as_view()),
    path('categorymeel/', CategoryMeelList.as_view()),
    path('categorymeel/<int:pk>', CategoryMeelDetail.as_view()),
    path('categoryfood/', CategoryFoodList.as_view()),
    path('categoryfood/<int:pk>', CategoryFoodDetail.as_view()),
    path('menu/', MenuList.as_view()),
    path('menu/<int:pk>', MenuDetail.as_view()),
    path('orderitem/', OrderItemList.as_view()),
    path('orderitem/<int:pk>', OrderItemDetail.as_view()),
    path('order/', OrderList.as_view()),
    path('order/<int:pk>', OrderDetail.as_view()),
]