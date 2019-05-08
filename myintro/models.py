from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)