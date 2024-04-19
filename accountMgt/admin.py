from django.contrib import admin

from accountMgt import models

# Register your models here.
admin.site.register(models.Employer)
admin.site.register(models.Recruiter)
admin.site.register(models.Jobseeker)
