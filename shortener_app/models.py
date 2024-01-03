from django.db import models

# Create your models here.
class Url(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    full_url = models.URLField()
    shortened_uri = models.URLField()

    def __str__(self):
        return(f'{self.shortened_uri} - {self.full_url}')