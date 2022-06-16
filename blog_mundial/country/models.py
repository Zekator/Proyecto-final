from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=40)
    country_id = models.IntegerField()

    def __str__(self):
        return f'Nombre del país: {self.name}'
