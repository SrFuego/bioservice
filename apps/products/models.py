# apps/products/models.py
# Python imports


# Django imports
from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify


# Third party apps imports
from stdimage.models import StdImageField
from stdimage.utils import UploadToAutoSlugClassNameDir
from stdimage.validators import MaxSizeValidator, MinSizeValidator


# Local imports


# Create your models here.
class Category(models.Model):
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    slug = models.SlugField(max_length=50, unique=True)
    title = models.CharField(
        max_length=50, unique=True, verbose_name="Título")
    eng_title = models.CharField(
        max_length=50, unique=True, verbose_name="Título en inglés")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, related_name="subcategories", verbose_name="Categoría")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    slug = models.SlugField(max_length=50, unique=True)
    title = models.CharField(
        max_length=50, unique=True, verbose_name="Título")
    eng_title = models.CharField(
        max_length=50, unique=True, verbose_name="Título en inglés")

    class Meta:
        verbose_name = "Subcategoría"
        verbose_name_plural = "Subcategorías"
        unique_together = ("title", "category",)

    def __str__(self):
        return "{0}, categoría: {1}".format(self.title, self.category.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Product(models.Model):
    code = models.CharField(max_length=30, unique=True, verbose_name="Código")
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
    name = models.CharField(max_length=50, verbose_name="Nombre")
    eng_name = models.CharField(
        max_length=50, verbose_name="Nombre en inglés")
    slug = models.SlugField(max_length=50)
    subcategory = models.ForeignKey(
        SubCategory, related_name="products", verbose_name="Subcategoría")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        unique_together = ("name", "subcategory",)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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
