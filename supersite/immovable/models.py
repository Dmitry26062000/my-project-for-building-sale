from django.db import models
from datetime import date


# Create your models here.
class contract(models.Model):
    Buyer = models.ForeignKey('users', on_delete=models.PROTECT, null=True)
    status = models.ForeignKey('status', on_delete=models.PROTECT, null=True)
    employee = models.ForeignKey('employee', on_delete=models.PROTECT, null=True)
    dateOfSign = models.DateField()
    appl=models.OneToOneField('application',on_delete=models.PROTECT, null=True)
    Resprice=models.IntegerField(default=3000)

class employee(models.Model):
    photoEmp = models.ImageField(upload_to="photos/")
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    depart = models.ForeignKey('department', on_delete=models.PROTECT, null=True)
    post = models.CharField(max_length=10)
    manager = models.ForeignKey('employee', on_delete=models.PROTECT, null=True)
    hire = models.DateField(auto_now_add=True)
class department(models.Model):
    name = models.CharField(max_length=50)

class status(models.Model):
    name = models.CharField(max_length=10)

class application(models.Model):
    email = models.CharField(max_length=20)
    Home = models.OneToOneField('home', on_delete=models.PROTECT, null=True)
class Home(models.Model):
    floor = models.CharField(max_length=3)
    Croom = models.CharField(max_length=3)
    area = models.CharField(max_length=10)
    balcony = models.BooleanField(default=False)
    numofkv = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    numofhome = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='photos/')
    price = models.IntegerField()


class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.ForeignKey('role', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    name = models.CharField(max_length=10)
    prommisse = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Meta:
    db_table = 'users'
