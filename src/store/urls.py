from django.urls import path
from .views import *

urlpatterns = [
    path('', list, name="home"),
    path('details/<int:pk>', details.as_view(), name="details"),
    path('list_restaurant/', list_restaurant, name="list_restaurant"),
    path('list_food/', list_food, name="list_food"),
    path('best_restaurant/', best_restaurant, name="best_restaurant"),
    path('best_food/', best_food, name="best_food"),
    path('search/', search, name='search'),
    path('search2/', search2, name='search2'),
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
    path('seareh2/', search21, name='seareh2'),
    path('rest_create/', rest_create, name='rest_create'),
    path('category1_create/', category1_create, name='category1_create'),
    path('category2_create/', category2_create, name='category2_create'),
    path('branch_create/', branch_create, name='branch_create'),
    path('menu_create/', menu_create, name='menu_create'),
    path('food_create/', food_create, name='food_create'),
    path('menu_edit/<int:pk>/', menu_edit, name='menu_edit'),
    path('rest_edit/<int:pk>/', rest_edit, name='rest_edit'),
    path('branch_edit/<int:pk>/', branch_edit, name='branch_edit'),
    path('cat1_edit/<int:pk>/', cat1_edit, name='cat1_edit'),
    path('cat2_edit/<int:pk>/', cat2_edit, name='cat2_edit'),
    path('food_edit/<int:pk>/', food_edit, name='food_edit'),
    path('menu_del/<int:pk>/', menu_del, name='menu_del'),
    path('rest_del/<int:pk>/', rest_del, name='rest_del'),
    path('branch_del/<int:pk>/', branch_del, name='branch_del'),
    path('cat1_del/<int:pk>/', cat1_del, name='cat1_del'),
    path('cat2_del/<int:pk>/', cat2_del, name='cat2_del'),
    path('food_del/<int:pk>/', food_del, name='food_del'),
    path('sss/', list_view, name='views'),
    path('orders/', orders, name='orders'),
    path('list_rest/', list_rest, name='list_rest'),
    path('list_branch/', list_branch, name='list_branch'),
    path('list_meel/', list_meel, name='list_meel'),
    path('list_foods/', list_foods, name='list_foods'),
    path('list_foodss/', list_foodss, name='list_foodss'),
    path('list_menu/', list_menu, name='list_menu'),
]
