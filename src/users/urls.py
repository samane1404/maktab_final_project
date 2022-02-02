from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('', home, name='users-home'),
                  path('register/', RegisterView.as_view(), name='users-register'),
                  path('register2/', RegisterView2.as_view(), name='manager-register'),
                  path('login/',
                       CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                               authentication_form=LoginForm), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
                  path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
                  path('password-reset-confirm/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
                       name='password_reset_confirm'),
                  path('password-reset-complete/',
                       auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
                       name='password_reset_complete'),
                  path('profile/', profile, name='users-profile'),
                  path('password-change/', ChangePasswordView.as_view(), name='password_change'),
                  path('list_user/', list_user, name='list_user'),
                  path('edit_user/<int:pk>/', edit_user, name='edit_user'),
                  path('delete_user/<int:pk>/', delete_user, name='delete_user'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
