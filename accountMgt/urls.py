from django.urls import path
from .views import  EmployerCreate

urlpatterns = [
    path('account', EmployerCreate.as_view(), name = 'EmployerCreate')
]