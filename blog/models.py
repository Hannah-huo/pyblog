from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()

class Blog(models.Model):
    content = models.TextField()
    authoer = models.CharField(max_length = 100)
    create_date = models.DateField()