# apps/texts/models.py
# Python imports


# Django imports
from django.db import models
from django.utils.text import slugify


# Third party apps imports


# Local imports


# Create your models here.
class Text(models.Model):
    title = models.CharField(
        max_length=50, unique=True, verbose_name="Título")
    eng_title = models.CharField(
        max_length=50, unique=True, verbose_name="Título en inglés")
    content = models.TextField(verbose_name="Contenido")
    eng_content = models.TextField(verbose_name="Contenido en inglés")
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Texto"
        verbose_name_plural = "Textos"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Testimony(models.Model):
    area = models.CharField(max_length=50, unique=True, verbose_name="Área")
    area_eng = models.CharField(
        max_length=50, unique=True, verbose_name="Área en inglés")
    description = models.TextField(verbose_name="Descripción")
    description_eng = models.TextField(verbose_name="Descripción en inglés")
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre")
    name_eng = models.CharField(
        max_length=50, unique=True, verbose_name="Nombre en inglés")

    class meta:
        verbose_name = "Testimonio"
        verbose_name_plural = "Testimonios"

    def __str__(self):
        return self.name
