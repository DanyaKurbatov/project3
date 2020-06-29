from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=50)
    start_quiz = models.DateTimeField()
    end_quiz = models.DateTimeField()
    description = models.CharField(max_length=200)
