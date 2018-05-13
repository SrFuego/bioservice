# apps/texts/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Testimony, Text


# Register your models here.
@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):

    list_display = ("name", "name_eng", "area", "area_eng",)
    list_filter = ("area", "area_eng",)
    ordering = ("-name",)
    search_fields = ("area", "area_eng",)


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):

    exclude = ("slug",)
    list_display = ("title", "content",)
    list_filter = ("title",)
    ordering = ("-title",)
    search_fields = ("title", "content",)
