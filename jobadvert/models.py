from django.db import models
from django_pandas.io import read_frame
from django_pandas.managers import DataFrameManager

# Create your models here.
class Job(models.Model):
    #code, name, description, sector, url, location ...
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    advertDate = models.CharField(max_length=25, default="")
    closingDate = models.CharField(max_length=25, default="")
    summary = models.TextField()
    employerId = models.ForeignKey("accountMgt.Employer", on_delete=models.CASCADE)

    #objects = DataFrameManager()
    def __str__(self):
        return self.title
    

class Skill(models.Model):
    #code, name, description, sector, url, location ...
    skillName = models.CharField(max_length=25)
    sector = models.CharField(max_length=25)

    def __str__(self):
        return self.skillName
    
class Advert(models.Model):
    #code, name, description, sector, url, location ...
    jobid = models.ForeignKey("Job", on_delete=models.CASCADE)
    skillId = models.ForeignKey("Skill", on_delete=models.CASCADE)

    def __str__(self):
        return self.jobid + " - " + self.skillId      