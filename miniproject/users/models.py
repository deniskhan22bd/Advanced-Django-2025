from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    ROLE_CHOICES = [ 
        ('admin', 'Admin'), 
        ('manager', 'Manager'), 
        ('employee', 'Employee'), 
    ] 
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    def __str__(self): 
        return f"{self.username} ({self.role})" 
    

class Profile(models.Model): 
    name = models.CharField(max_length=255) 
    email = models.EmailField() 
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True) 
    def __str__(self):
        return self.name