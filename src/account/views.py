from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    return render(request, 'home.html')

def admin_required(login_url=None):
    return user_passes_test(lambda u: u.is_superuser, login_url=login_url)


def admin(request):
    return render(request, 'account/profile_admin.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'account/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


class RegisterView1(View):
    form_class = RegisterForm1
    initial = {'key': 'value'}
    template_name = 'account/register_manager.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)

            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')

        return super().dispatch(request, *args, **kwargs)


class CustomLoginView1(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)

            self.request.session.modified = True

        return super(CustomLoginView1, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')

        return super().dispatch(request, *args, **kwargs)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'account/password_reset.html'
    email_template_name = 'account/password_reset_email.html'
    subject_template_name = 'account/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    heading_message = 'Formset Demo'
    user_form = UpdateUserForm(request.POST, instance=request.user)
    profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
    formset = AddressFormset(request.POST)
    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid() and formset.is_valid():
            for form in formset:
                address = form.cleaned_data.get('address')
                if address:
                    Address(address=address).save()
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        formset = AddressFormset(request.GET or None)

    return render(request, 'account/profile.html', {'user_form': user_form, 'profile_form': profile_form, 'formset': formset, 'heading': heading_message})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile_manager(request):
    user_form = UpdateUserForm(request.POST, instance=request.user)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile_manager')
    else:
        user_form = UpdateUserForm(instance=request.user)
    return render(request, 'account/profile_manager.html',
                  {'user_form': user_form})


def list_user(request):
    context = {"customer": Customer.objects.filter(is_staff=False)}
    return render(request, "account/list_user.html", context)


def list_manager(request):
    context = {"customer": Customer.objects.filter(is_staff=True)}
    return render(request, "account/list_manager.html", context)






