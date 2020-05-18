from django.db import models

class Link(models.Model):
    url = models.CharField(max_length=60)
    shortlink = models.CharField(max_length=6)
    def __str__(self):
        return self.url
    