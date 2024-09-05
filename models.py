from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=400)
 
    def __str__(self):
        return str(self.title)
