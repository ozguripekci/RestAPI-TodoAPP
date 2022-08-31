from turtle import done
from django.db import models


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=100)
    description = models.TextField()
    TITLE = (
        ('1', 'High'),
        ('2', 'Medium'),
        ('3',  'Low'),
    )
    priority = models.CharField(max_length=50, choices=TITLE, default=3)
    done = models.BooleanField()
    updateDate = models.DateTimeField(auto_now=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

    
