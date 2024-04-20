from django.urls import path
from jobadvert import  views

urlpatterns = [
    #path('v1/job/', views.EmployerCreate.as_view(), name = 'EmployerCreate'),
    path('v1/skill/', views.get_skill_form, name='get_skill_form'),
    path('v1/skill/add', views.submit_skill, name='submit_skill'),
    path('v1/job', views.get_job_form, name='get_job_form'),
    path('v1/job/posting', views.job_Posting, name='job_Posting'),
    path('v1/job/currentopenings', views.current_jobs, name='job_Current'),
    path('v1/job/charts', views.get_job_charts, name='get_job_charts'),
    path('V1/apply', views.get_job_apply, name='get_job_apply'),

    path('jobs/', views.JobListView.as_view(), name='job-list'),
    path('jobs/create/', views.JobCreateView.as_view(), name='job-create'),
    path('jobs/update/<int:pk>', views.JobModifyView.as_view(), name='job-update'),
    #path('jobs/remove/<int:pk>', views.JobRemoveView.as_view(), name='job-delete'),
]