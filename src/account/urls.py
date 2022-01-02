from django.urls import path, include
from .views import *


urlpatterns = [
    path('customer/', CustomerList.as_view()),
    path('customer/<int:pk>', CustomerDetail.as_view()),
    path('manager/', ManagerList.as_view()),
    path('manager/<int:pk>', ManagerDetail.as_view()),
]