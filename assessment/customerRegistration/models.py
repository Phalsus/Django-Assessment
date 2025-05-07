from django.db import models
import uuid

# Create your models here.


class customerFeedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
