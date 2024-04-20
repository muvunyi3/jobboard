from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Job, Skill, Advert
from accountMgt.models import Employer
from .serialize import JobSerializer, SkillSerializer, AdvertSerializer
import pandas as pd

# Create your views here.
def get_job_form(request):
    employers = Employer.objects.all()
    return render(request, 'jobadvert/advert.html', {'employers':employers})
def get_job_charts(request):
    employers = Employer.objects.all()
    employers_data = list(employers.values())
    employers_df = pd.DataFrame(employers_data)
    employers_df.rename(columns={'id': 'employerId'}, inplace=True)
    employers_df = employers_df[['name', 'employerId']]
    print("employers_df: ")
    print(employers_df)
    jobs = Job.objects.all()
    jobs_data= list(jobs.values())
    jobs_df = pd.DataFrame(jobs_data)
    jobs_df.rename(columns={'employerId_id':'employerId'}, inplace=True)
    jobs_df = jobs_df[['id', 'title', 'category', 'employerId']]
    print("jobs_df: \n")
    print(jobs_df)
    jobs_by_employer_df = pd.merge(jobs_df, employers_df, on='employerId', how='inner')
    print("After Merging: ")
    print(jobs_by_employer_df)
    #jobs_by_employer_df.groupby('employerId')['id'].count().reset_index()
    employer_counts = jobs_by_employer_df.groupby('employerId').size().reset_index(name='count')
    
    employer_counts_df = pd.merge(employer_counts, employers_df, on='employerId', how='inner')
    # Display the counts
    print('employer_counts_df')
    print(employer_counts_df)
    
    print("After groupby: ")
    print(jobs_by_employer_df.columns)
    #if not jobs_df.empty and employers_df.empty:
        #jobs_by_employer_df = pd.merge(jobs_df, employers_df, on='employerId', how='inner')
        #print("After Merging: ")
        #print(jobs_by_employer_df)

        #convert to list of dictionaries
    empJobsDict = jobs_by_employer_df.to_dict(orient='records')
    empCountsDict = employer_counts_df.to_dict(orient='records')
    

    return render(request, 'jobadvert/jobcharts.html', {'empJobsDict':empJobsDict, 'empCountsDict':empCountsDict})

def job_Posting(request):   
    if request.method == 'POST':
      
        #jobseeker = Jobseeker.objects.create(name=data.get('name'), title=data.get('title'), email=data.get('email'), phone=data.get('phone'))
        print("I am called ...")
        print("name: " + request.POST.get('title'))
        print( request.POST.get('employerId'))

        title = request.POST.get('title'),
        jobType = request.POST.get('jobType'),
        category = request.POST.get('category'),
        summary = request.POST.get('summary'),
        advertDate = request.POST.get('advertDate'),
        closingDate = request.POST.get('closingDate'),
        employerId= request.POST.get('employerId'),
        employer = Employer.objects.get(id=int(employerId[0]))
        print(employer)
        #skillId = request.POST.get('skillId'),
        
        job = Job.objects.create( title=title[0], type=jobType[0],summary=summary[0], category=category[0], advertDate=advertDate[0],closingDate=closingDate[0], employerId=employer)
        print(employer)
        #Advert = Advert.objects.create( jobid=job.id, skillId=jobType)
        return JsonResponse({'status': job.title + ' is recorded successfully!'})  
    else:
        return JsonResponse({'status': 'Invalid request'}, status=400)

def get_skill_form(request):
    skills = Skill.objects.all()
    return render(request, 'jobadvert/skill.html', {'skills': skills})

def submit_skill(request):
    if request.method == 'POST':
        skillName= request.POST.get('skill')
        sector= request.POST.get('sector')
        skill = Skill.objects.create( skillName=skillName, sector=sector )
        
        return JsonResponse({'status': 'Record successful!', 'skillName':skill.skillName, 'sector':skill.sector})  
    else:
        return JsonResponse({'status': 'Invalid request'}, status=400)


def current_jobs(request): 
    jobs = Job.objects.all()
    print(jobs)
    return render(request, 'jobadvert/job.html', {'jobs': jobs})  
  
# Create API views here.
class JobCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all() 
    serializer_class = JobSerializer


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    http_method_names = ['get']  


class SkillsCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillsModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all() 
    serializer_class = SkillSerializer

class SkillsListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    http_method_names = ['get']

class AdvertCreateView(generics.ListCreateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class AdvertModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advert.objects.all() 
    serializer_class = AdvertSerializer  

class AdvertListView(generics.ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    http_method_names = ['get']

def get_job_apply(request):
    return render(request,"blog/index.html")