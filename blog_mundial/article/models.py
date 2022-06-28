from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=20)
    article_id = models.IntegerField()
    #article_content = models.TextField(max_length=1200)
    article_content = RichTextField('Escriba aqui su articulo')


    def __str__(self):
        return f'Nombre del Artículo: {self.name} País sobre el artículo: {self.country} '