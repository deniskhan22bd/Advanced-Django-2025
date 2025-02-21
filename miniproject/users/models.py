from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    ROLE_CHOICES = [ 
        ('admin', 'Admin'),
        ('trader', 'Trader'),  
        ('representative', 'Representative'), 
        ('customer', 'Customer'), 
    ] 
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True) 
    def __str__(self): 
        return f"{self.username} ({self.role})" 