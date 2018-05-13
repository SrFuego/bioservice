# apps/services/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Service


# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    exclude = ("slug",)
    list_display = (
        "name", "description", "image_1_admin_thumbnail", "is_active",)
    readonly_fields = (
        "image_1_admin_thumbnail", "image_2_admin_thumbnail",
        "image_3_admin_thumbnail")
    fields = (
        "name", "eng_name", "description", "eng_description", "image_1",
        "image_1_admin_thumbnail", "image_2", "image_2_admin_thumbnail",
        "image_3", "image_3_admin_thumbnail", "is_active",)
    list_filter = ("is_active",)
    ordering = ("-name",)
    search_fields = ("name",)
