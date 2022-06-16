from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=20)
    article_id = models.IntegerField()
    article_content = models.TextField()

    def __str__(self):
        return f'Nombre del Artículo: {self.name} País sobre el artículo: {self.country} '