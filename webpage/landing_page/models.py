from pickletools import read_uint1
from django.db import models

# Create your models here.

class Contact(models.Model):
    """model to store customer contact info"""

    name = models.CharField(max_length= 100)
    email = models.EmailField()


    def __str__(self):
        return self.name

    def get_email(self):
        return self.email
