from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Articale(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=False)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    
    
    
        
    
