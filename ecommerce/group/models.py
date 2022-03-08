from django.db import models

# Create your models here.

class employee1(models.Model):
    ename = models.CharField(max_length=100)
    eemail = models.CharField(max_length=100)
    econtact = models.CharField(max_length=100)
    eage = models.IntegerField()
    class  Meta:
        db_table = 'employee1'

