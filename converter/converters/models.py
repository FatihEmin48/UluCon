from django.db import models

# Create your models here.
class Converter(models.Model):
    name = models.CharField(max_length=100, verbose_name='Converter Name')
    description = models.TextField(verbose_name='Converter Desc.')
    image = models.CharField(max_length=50, verbose_name='Converter img.')
    link = models.TextField(verbose_name='Converter Url')

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/img/' + self.image

    