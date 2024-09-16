from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
class Task(models.Model):
    STATUS_CHOICES = [
     ('pending', 'Pending'),
     ('in_progress', 'In Progress'),
     ('completed', 'Completed'),
    ]
    PRIORITY_CHOICES = [
     ('low', 'Low'),
     ('medium', 'Medium'),
     ('high', 'High'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=10)