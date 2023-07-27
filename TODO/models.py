from django.db import models

class todo_list(models.Model):
    user_name = models.CharField( max_length=50)
    name = models.CharField( max_length=50)
    desc = models.CharField( max_length=200)
    end_time = models.CharField( max_length=200)
    status = models.CharField( max_length=200)
    

# Create your models here.
