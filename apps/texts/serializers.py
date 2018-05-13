# apps/texts/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework import serializers


# Local imports
from .models import Testimony, Text


# Create your serializers here.
class TestimonySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Testimony
        fields = (
            "area", "area_eng", "description", "description_eng", "name",
            "name_eng", "url",)


class TextSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Text
        fields = (
            "content", "eng_content", "eng_title", "slug", "title", "url",)
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
