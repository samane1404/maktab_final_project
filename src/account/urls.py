from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from .forms import *

urlpatterns = [
    path('', home, name='users-home'),
    path('profile_admin/', admin, name='profile_admin'),
    path('profile_manager/', profile_manager, name='profile_manager'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('register_manager/', RegisterView1.as_view(), name='manager-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='account/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('login_manager/', CustomLoginView1.as_view(redirect_authenticated_user=True, template_name='account/login_manager.html',
                                           authentication_form=LoginForm1), name='login_manager'),
    path('login_admin/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='account/login_admin.html',
                                           authentication_form=LoginForm), name='login_admin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('profile/', profile, name='users-profile'),
    path('list_user/', list_user, name='list_user'),
    path('list_manager/', list_manager, name='list_manager'),

]
