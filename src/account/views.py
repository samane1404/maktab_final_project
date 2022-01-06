from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .forms import LoginForm
from .models import *
from .serializer import *
from .permission import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy



# Create your views
def home(x):
    return render(x, 'home.html')



class SignUpView(generics.CreateAPIView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAdminUser]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAdminUser]
    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
    def perform_desrtoy(self, serializer):
        serializer.save(owner=self.request.user)

class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAdminUser]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAdminUser]
    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
    def perform_desrtoy(self, serializer):
        serializer.save(owner=self.request.user)

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAdminUser]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAdminUser]
    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
    def perform_desrtoy(self, serializer):
        serializer.save(owner=self.request.user)



class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)