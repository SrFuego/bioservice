# apps/texts/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import Testimony, Text
from .serializers import TestimonySerializer, TextSerializer


# Create your views here.
class TestimonyViewSet(ModelViewSet):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer


class TextViewSet(ModelViewSet):
    """
    API endpoint that allows texts to be viewed or edited.
    """
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    lookup_field = "slug"
