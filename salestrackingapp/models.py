from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.contrib.auth.models import User

class Userdata(models.Model):
    User_id=models.IntegerField(auto_created=True,primary_key=True)
    email = models.CharField(max_length=50, null=True,unique=True)
    phonenumber=models.IntegerField(default=0,unique=True)
    Age=models.IntegerField(default=0)

class dailystatus(models.Model):
    Area_visited=models.CharField(max_length=100, null=True)
    total_persons_approched=models.IntegerField(default=0)
    number_converted=models.IntegerField(default=0)
    created_on=models.DateTimeField(auto_now_add=True, blank=True)
    User_f_id=models.ForeignKey('Userdata',on_delete=models.CASCADE)

gen=[
    ('male','Male'),
    ('female','FeMale'),
    ('other','Other'),
]
class customerdata(models.Model):
    Name=models.CharField(max_length=100, null=True)
    DOB=models.CharField(max_length=100, null=True)
    Age=models.CharField(max_length=100, null=True)
    Gender=models.CharField(max_length=50,choices=gen,default='male')
    Family_member=models.IntegerField(default=0)
    created_on=models.DateTimeField(auto_now_add=True, blank=True)
    Is_client=models.BooleanField(default=False)
    User_c_id=models.ForeignKey('Userdata',on_delete=models.CASCADE)