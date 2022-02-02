from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('', Home.as_view, name='users-home'),
                  path('search/', search, name='search'),
                  path('best_food/', best_food, name='best_food'),
                  path('details_menu/<slug:slug>/', MenuDetail.as_view(), name='details_menu'),
                  path('create_restaurant/', create_restaurant, name='create_restaurant'),
                  path('edit_restaurant/<int:pk>/', edit_restaurant, name='edit_restaurant'),
                  path('delete_restaurant/<int:pk>/', delete_restaurant, name='delete_restaurant'),
                  path('create_branch/', create_branch, name='create_branch'),
                  path('edit_branch/<int:pk>/', edit_branch, name='edit_branch'),
                  path('delete_branch/<int:pk>/', delete_branch, name='delete_branch'),
                  path('create_category_food/', create_category_food, name='create_category_food'),
                  path('edit_category_food/<int:pk>/', edit_category_food, name='edit_category_food'),
                  path('delete_category_food/<int:pk>/', delete_category_food, name='delete_category_food'),
                  path('create_category_meel/', create_category_meel, name='create_category_meel'),
                  path('edit_category_meel/<int:pk>/', edit_category_meel, name='edit_category_meel'),
                  path('delete_category_meel/<int:pk>/', delete_category_meel, name='delete_category_meel'),
                  path('create_food/', create_food, name='create_food'),
                  path('edit_food/<int:pk>/', edit_food, name='edit_food'),
                  path('delete_food/<int:pk>/', delete_food, name='delete_food'),
                  path('create_menu/', create_menu, name='create_menu'),
                  path('edit_menu/<int:pk>/', edit_menu, name='edit_menu'),
                  path('delete_menu/<int:pk>/', delete_menu, name='delete_menu'),
                  path('menu_manager', menu_manager, name='menu_manager'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
