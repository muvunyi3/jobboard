from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Employer, Recruiter, Jobseeker
from django.views.generic.edit import CreateView
from .serialize import EmployerSerializer, RecruiterSerializer, JobseekerSerializer

# Create your views here.
class EmployerCreate(CreateView):  
    model = Employer  
    fields = '__all__' 
    def get_success_url(self):
        return JsonResponse({'status': 'Record successful!'})

class RecruiterCreate(CreateView):  
    model = Recruiter  
    fields = '__all__' 
    
class JobseekersCreate(CreateView):  
    model = Jobseeker 
    fields = '__all__'  

# Create Normal Views
def get_jobseeker_form(request):
    return render(request, 'accountMgt/jobseeker.html')

def submit_jobseeker_data(request):   
    if request.method == 'POST':
      
        #jobseeker = Jobseeker.objects.create(name=data.get('name'), title=data.get('title'), email=data.get('email'), phone=data.get('phone'))
        print("I am called ...")
        print("name: " + request.POST.get('name'))
        name = request.POST.get('name'),
        title = request.POST.get('title'),
        email = request.POST.get('email1'),
        phone = request.POST.get('phone'),
        gender = request.POST.get('gender'),
        
        jobseeker = Jobseeker.objects.create(name=name[0], title=title[0],  phone=phone[0], email=email[0], gender=gender[0])
        return JsonResponse({'status': 'Record successful!'})
        
    else:
        return JsonResponse({'status': 'Invalid request'}, status=400)
    
# Create API views here.
class EmployerCreateView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class RecruiterCreateView(generics.ListCreateAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class JobseekersCreateView(generics.ListCreateAPIView):
    queryset = Jobseeker.objects.all()
    serializer_class = JobseekerSerializer


class EmployerModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all() 
    serializer_class = EmployerSerializer

class RecruiterModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recruiter.objects.all() 
    serializer_class = RecruiterSerializer

class JobseekersModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jobseeker.objects.all() 
    serializer_class = JobseekerSerializer

class EmployerListView(generics.ListAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    http_method_names = ['get']    

class RecruiterListView(generics.ListAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    http_method_names = ['get']

class JobseekersListView(generics.ListAPIView):
    queryset = Jobseeker.objects.all()
    serializer_class = JobseekerSerializer
    http_method_names = ['get']