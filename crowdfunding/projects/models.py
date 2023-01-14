from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField() #to check if the project is open
    date_created = models.DateTimeField(auto_now_add=True) #auto now add, add date time
    owner = models.CharField(max_length=200)
    
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='pledges')
    supporter = models.CharField(max_length=200)