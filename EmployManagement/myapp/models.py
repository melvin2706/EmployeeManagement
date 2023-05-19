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

class Post(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.name

class Holiday(models.Model):
    date_start = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)

class Authorization(models.Model):
    motif = models.CharField(max_length = 150)
    holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True)
    birth_place = models.CharField(max_length = 150, null=True)
    sex = models.CharField(max_length = 150, null=True)
    contact = models.IntegerField(null=True)
    matrimonial_situation = models.CharField(max_length = 150, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    authotization = models.ForeignKey(Authorization, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username +' '+ str(self.service)
    

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 150)
    description = models.TextField()
    responsible = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name+ ' '+str(self.responsible.username)
    
     