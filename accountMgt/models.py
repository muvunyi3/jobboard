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