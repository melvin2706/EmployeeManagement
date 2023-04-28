from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Department(models.Model):
    """Model definition for department."""
    name = models.CharField(max_length = 150)
    description = models.TextField()
    
    def __str__(self):
        """Unicode representation of department."""
        return self.name

class Service(models.Model):
    """Model definition for service."""
    name = models.CharField(max_length = 150)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        """Unicode representation of service."""
        return self.name


class Project(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    date_start = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Meeting(models.Model):
    subject = models.CharField(max_length = 150)
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    

    def __str__(self):
        return self.subject


class CustomUser(AbstractUser):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)