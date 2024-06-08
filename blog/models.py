from django.db import models
from django.contrib.auth.models import User

class Emp(models.Model):
    User = models.ForeignKey(User, on_delete = models.SET_NULL ,null= True,blank= True)
    name = models.CharField(max_length = 200)
    emp_id = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 150)
    working = models.BooleanField(default= 200)
    department = models.CharField(max_length = 10)
    pic = models.ImageField(upload_to="picture" ,null=True, blank=True)
    def __str__(self):
        return self.name
    
   