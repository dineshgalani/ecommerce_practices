import email
from django.db import models

# Create your models here.

class Hr(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)

    class Meta:
        db_table = 'hr'