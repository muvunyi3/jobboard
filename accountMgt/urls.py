from django.urls import path
from accountMgt import  views

urlpatterns = [
    path('v1/employers/', views.EmployerCreate.as_view(), name = 'EmployerCreate'),
    path('v1/jobseekers/', views.get_jobseeker_form, name='get_jobseeker_form'),
    path('v1/jobseekers/add', views.submit_jobseeker_data, name='submit_jobseeker_data'),

    path('employers/', views.EmployerListView.as_view(), name='employer-list'),
    path('employers/create/', views.EmployerCreateView.as_view(), name='employer-create'),
    path('employers/update/<int:pk>', views.EmployerModifyView.as_view(), name='employer-update'),

    path('recruiters/', views.RecruiterListView.as_view(), name='recruiter-list'),
    path('recruiters/create/', views.RecruiterCreateView.as_view(), name='recruiter-create'),
    path('recruiters/update/<int:pk>', views.RecruiterModifyView.as_view(), name='recruiter-update'),

    path('jobseekers/', views.JobseekersListView.as_view(), name='jobseeker-list'),
    path('jobseekers/create/', views.JobseekersCreateView.as_view(), name='jobseeker-create'),
    path('jobseekers/update/<int:pk>', views.JobseekersModifyView.as_view(), name='jobseeker-update'),

]