from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    ROLE_CHOICES = [ 
        ('admin', 'Admin'),
        ('recruiter', 'Recruiter'),  
        ('job seeker', 'Job Seeker'), 
    ] 
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='job seeker')
    def __str__(self): 
        return f"{self.username} ({self.role})" 