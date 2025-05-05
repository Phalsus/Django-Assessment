from django.db import models

# Create your models here.


class customerFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
