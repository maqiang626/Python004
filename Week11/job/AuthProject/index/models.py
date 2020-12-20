from django.db import models

# Create your models here.


class Type(models.Model):
    typename = models.CharField(max_length=50)
