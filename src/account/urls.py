from django.urls import path, include
from .views import *
from viewss import *


urlpatterns = [
    path('', home, name='home'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('customer/', CustomerList.as_view(), name='customer'),
    path('customer/<int:pk>', CustomerDetail.as_view()),
    path('manager/', ManagerList.as_view(), name='manager'),
    path('manager/<int:pk>', ManagerDetail.as_view()),
    path('address/', AddressList.as_view(), name='address'),
    path('address/<int:pk>', AddressDetail.as_view()),
]