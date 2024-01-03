from django.db import models

# Create your models here.
class Url(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    long_url = models.URLField()
    short_url = models.URLField()