from concurrent.futures.process import _python_exit
from platform import python_implementation
from django.db import models

# Create your models here.


# class Person(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     phone_no = models.CharField(max_length=25)


class Note(models.Model):
    note_title = models.CharField(max_length=200)
    note_content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
