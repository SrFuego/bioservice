# apps/products/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework import serializers


# Local imports
from .models import Category, Product, SubCategory


# Create your serializers here.
class SubCategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = SubCategory
        fields = ("title", "eng_title", "category", "slug", "products")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}

    def get_products(self, obj):
        return ProductSerializer(
            obj.products.filter(is_active=True), many=True).data


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SlugField(read_only=True)
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("url", "title", "eng_title", "subcategories", "slug",)
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}

    def get_subcategories(self, obj):
        return SubCategorySerializer(
            obj.subcategories.filter(is_active=True), many=True).data


class ProductSerializer(serializers.ModelSerializer):
    image_1 = serializers.CharField(source="image_1.url")
    image_1_thumbnail = serializers.CharField(source="image_1.thumbnail.url")
    image_2 = serializers.CharField(source="image_2.url")
    image_2_thumbnail = serializers.CharField(source="image_2.thumbnail.url")
    image_3 = serializers.CharField(source="image_3.url")
    image_3_thumbnail = serializers.CharField(source="image_3.thumbnail.url")
    slug = serializers.SlugField(read_only=True)
    subcategory = serializers.SlugRelatedField(
        read_only=True, slug_field="slug")

    class Meta:
        model = Product
        fields = (
            "id", "name", "eng_name", "code", "subcategory", "description",
            "eng_description", "image_1", "image_1_thumbnail", "image_2",
            "image_2_thumbnail", "image_3", "image_3_thumbnail", "slug",)
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
