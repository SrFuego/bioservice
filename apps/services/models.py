# apps/services/models.py
# Python imports


# Django imports
from django.db import models
from django.utils.text import slugify
from django.utils.html import format_html


# Third party apps imports
from stdimage.models import StdImageField
from stdimage.utils import UploadToAutoSlugClassNameDir
from stdimage.validators import MaxSizeValidator, MinSizeValidator


# Local imports


# Create your models here.
class Service(models.Model):

    description = models.TextField(verbose_name="Descripción")
    eng_description = models.TextField(verbose_name="Descripción en inglés")
    image_1 = StdImageField(
        upload_to=UploadToAutoSlugClassNameDir(populate_from="name"),
        validators=[MinSizeValidator(400, 250), MaxSizeValidator(1000, 1000)],
        variations={"thumbnail": (400, 250)}, verbose_name="Imagen Principal")
    image_2 = StdImageField(
        blank=True,
        upload_to=UploadToAutoSlugClassNameDir(populate_from="name"),
        validators=[MinSizeValidator(400, 250), MaxSizeValidator(1000, 1000)],
        variations={"thumbnail": (400, 250)},
        verbose_name="Imagen 2 (opcional)")
    image_3 = StdImageField(
        blank=True,
        upload_to=UploadToAutoSlugClassNameDir(populate_from="name"),
        validators=[MinSizeValidator(400, 250), MaxSizeValidator(1000, 1000)],
        variations={"thumbnail": (400, 250)},
        verbose_name="Imagen 3 (opcional)")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre")
    eng_name = models.CharField(
        max_length=50, unique=True, verbose_name="Nombre en inglés")
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)

    def image_1_admin_thumbnail(self):
        if self.image_1:
            return format_html(
                "<img src='{0}' alt='{1}'>", self.image_1.thumbnail.url,
                self.name)
        else:
            return "Sin imagen"

    def image_2_admin_thumbnail(self):
        if self.image_2:
            return format_html(
                "<img src='{0}' alt='{1}'>", self.image_2.thumbnail.url,
                self.name)
        else:
            return "Sin imagen"

    def image_3_admin_thumbnail(self):
        if self.image_3:
            return format_html(
                "<img src='{0}' alt='{1}'>", self.image_3.thumbnail.url,
                self.name)
        else:
            return "Sin imagen"
