from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(max_length=500, unique=True)
    updated_on = models.DateField(auto_now=True)


    def __str__(self):
        return self.title