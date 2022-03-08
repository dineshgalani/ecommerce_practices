from operator import sub
from turtle import update
from unicodedata import category
from django.db import models

# Create your models here.

#this class product create data table in postgres sql you have to first migrate it in cmd for make change then for shownig in admin pannel you have to regester in admin.py of this app then it will see in admin pannel onsite
class product(models.Model):
    product_name = models.CharField(max_length=20,null=True)
    product_price = models.IntegerField(null=True)
    product_description = models.TextField(max_length=200,null=True)
    product_qty = models.IntegerField(null=True)
    product_color = models.CharField(max_length=10,null=True)
    created_at = models.DateTimeField(auto_now_add=True ,null=True)
    updated_at = models.DateTimeField(auto_now_add=True ,null=True)
    product_status = models.BooleanField(default=True,null=True)

#this class category is seprate group from product    
class category(models.Model):
#to connect this two table we have to create chile class of product as catedory
#class category(product):
    category_name = models.CharField(max_length=20,null=True)
    category_description = models.TextField(max_length=200,null=True)
    subcategory_name = models.CharField(max_length=20,null=True)
    class Meta:
        db_table = 'category'