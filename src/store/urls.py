from django.urls import path, include

urlpatterns = [
    path('v2/', include('rest_framework.urls'))
]