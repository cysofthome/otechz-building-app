from django.db import models
from django .conf import settings
from django .utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date =timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    
    
class Biodata(models.Model):
    sure_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    midle_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    phone = models.IntegerField()
    contact_addres = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    
    
    def publish(self):
        self.published_date =timezone.now()
        self.save()
        
        
    def __str__(self):
        return self.midle_name