from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# to be able to do that


class Expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    itemname=models.CharField(max_length=100)
    quantity=models.CharField(max_length=40)
    price=models.IntegerField()
    date=models.DateField()
    

class TaskModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    start=models.DateField()
    end=models.DateField()
    note=models.CharField(max_length=300)


class ProfileModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    img=models.ImageField(upload_to='profileimg')
    desc=models.TextField(max_length=150)
    occupation=models.CharField(max_length=100)
    martial=models.CharField(max_length=50)
    

class UserLogin(models.Model):
    ulname=models.CharField(max_length=70)
    ulpassword=models.CharField(max_length=80)
 

class UserCreation(models.Model):
    uname=models.CharField(max_length=100,primary_key=True)
    upw=models.CharField(max_length=200)


class GroupName(models.Model):
    gname=models.ForeignKey(UserCreation,on_delete=models.CASCADE)
    groupname=models.CharField(max_length=200,default="")
    