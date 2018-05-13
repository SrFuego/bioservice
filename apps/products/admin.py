# apps/products/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Category, Product, SubCategory


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    list_display = ("title", "eng_title", "is_active",)
    fields = ("title", "eng_title", "is_active",)
    list_filter = ("is_active",)
    ordering = ("-title",)
    search_fields = ("title", "eng_title")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    list_display = (
        "name", "code", "subcategory", "image_1_admin_thumbnail", "is_active",)
    readonly_fields = (
        "image_1_admin_thumbnail", "image_2_admin_thumbnail",
        "image_3_admin_thumbnail")
    fields = (
        "name", "eng_name", "code", "subcategory", "description",
        "eng_description", "image_1", "image_1_admin_thumbnail", "image_2",
        "image_2_admin_thumbnail", "image_3", "image_3_admin_thumbnail",
        "is_active",)
    list_filter = ("subcategory", "is_active",)
    ordering = ("-name",)
    search_fields = ("name", "eng_name", "code")


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    list_display = ("title", "eng_title", "category", "is_active",)
    fields = ("title", "eng_title", "category", "is_active",)
    list_filter = ("is_active", "category",)
    ordering = ("-title",)
    search_fields = ("title", "eng_title")
