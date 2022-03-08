from django.db import models

# Create your models here.

class task(models.Model):
    task_name = models.CharField(max_length=200)
    task_desctription = models.TextField()

    class Meta:
        db_table = 'task'