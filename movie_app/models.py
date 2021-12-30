from django.db import models

class Models(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()