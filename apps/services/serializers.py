# apps/services/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework import serializers


# Local imports
from .models import Service


# Create your serializers here.
class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    image_1 = serializers.CharField(source="image_1.url")
    image_1_thumbnail = serializers.CharField(source="image_1.thumbnail.url")
    image_2 = serializers.CharField(source="image_2.url")
    image_2_thumbnail = serializers.CharField(source="image_2.thumbnail.url")
    image_3 = serializers.CharField(source="image_3.url")
    image_3_thumbnail = serializers.CharField(source="image_3.thumbnail.url")
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Service
        fields = (
            "url", "name", "eng_name", "description", "eng_description",
            "image_1", "image_1_thumbnail", "image_2", "image_2_thumbnail",
            "image_3", "image_3_thumbnail", "slug",)
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
