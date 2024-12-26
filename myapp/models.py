from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50)
    category_id = models.IntegerField(default=1)
    ngo = models.CharField(max_length=100)
    details = models.TextField(max_length=10000)
    date = models.DateTimeField(max_length=50)
    city = models.CharField(max_length=50, default='Delhi')
    address = models.CharField(max_length=1000, default='Delhi')

class Category(models.Model):
    name = models.CharField(max_length=100)

class EventRegistration(models.Model):
    eventid = models.ForeignKey(Event, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    
