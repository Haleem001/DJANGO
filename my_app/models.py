from concurrent.futures.process import _python_exit
from platform import python_implementation
from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField( max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=25)
    
