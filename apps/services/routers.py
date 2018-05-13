# apps/services/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import ServiceViewSet


# Create your routers here.
services = (
    (r"services", ServiceViewSet),
)
