from calendar import c
from importlib.util import resolve_name
from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.

class Role(models.Model):
    role_name = models.CharField(max_length=50,null=True)
    role_description =models.TextField(max_length=100,null=True)
    class Meta:
        db_table = 'role'

#this roleid is used as forein key in employee
class Employee(Role):
    employee_name = models.CharField(max_length=201,null=True)
    employee_email = models.CharField(max_length=50,null=True)
    employee_password = models.CharField(max_length=50,null=True)
    employee_phone = models.IntegerField(null=True)
    employee_address = models.TextField(null=True)
    employee_dob = models.DateField(null=True)
    class Meta:
        db_table = 'employee'

class student(models.Model):
    #this sentence will do as above table this will create one to one relation-ship with student and rol
    #Role = models.ForeignKey(Role,on_delete=models.CASCADE)
    Role = models.OneToOneField(Role,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=50)
    student_password = models.CharField(max_length=50)
    student_phone = models.CharField(max_length=50)
    student_address = models.TextField()
    student_dob = models.DateField()
    class Meta:
        db_table = 'student'

class customer(models.Model):
    customer_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'customer'

class product(models.Model):
    CATEGORY = (('indoor','indoor'),('outdoor','outdoor'))
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_categotry = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'product'

class order(models.Model):
    STATUS = (('pending','pending'),('od','od'),('delivered','delivered'))
    customer = models.ForeignKey(customer,null=True,on_delete=models.SET_NULL)
    product  = models.ForeignKey(product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,null=True,choices=STATUS)
    class Meta:
        db_table = 'order'