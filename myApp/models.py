from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    cat_name=models.CharField(max_length=20)


    def __str__(self):
        return self.cat_name

class Products(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    price=models.CharField(max_length=12)
    image=models.ImageField(upload_to='phone',null=True,blank=True)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,null=True,blank=True)
    us=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.name
    

class Profile(models.Model):
    us = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    image=models.ImageField(upload_to='profilepic')    

    def __str__(self):
        return str(self.us)


