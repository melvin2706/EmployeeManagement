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


class CustomUser(AbstractUser):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    
    
    