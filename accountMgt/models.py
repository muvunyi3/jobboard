from django.db import models

# Create your models here.
class Employer(models.Model):
    #code, name, description, sector, url, location ...
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Recruiter(models.Model):
    #code, name, description, sector, url, location ...
    name = models.CharField(max_length=255,default="")
    title = models.CharField(max_length=25)
    email = models.EmailField
    phone = models.CharField(max_length=30)
    employerId = models.ForeignKey("Employer", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Jobseeker(models.Model):
    #code, name, description, sector, url, location ...
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=25)
    email = models.EmailField
    phone = models.CharField(max_length=30)
    profile = models.CharField(max_length=50)
    resume = models.CharField(max_length=50)

    def __str__(self):
        return self.name    