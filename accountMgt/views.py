from django.shortcuts import render
from .models import Employer
from django.views.generic.edit import CreateView

# Create your views here.
class EmployerCreate(CreateView):  
    model = Employer  
    fields = '__all__' 
    
