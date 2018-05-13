# apps/texts/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import TestimonyViewSet, TextViewSet


# Create your routers here.
texts = (
    (r"testimonials", TestimonyViewSet),
    (r"texts", TextViewSet)
)
