from django.db import models

class Models(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    sum_money = models.IntegerField(default=1000000)

    def __str__(self):
        return f'{self.name} - {self.rating}%'