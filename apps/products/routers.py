# apps/products/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import CategoryViewSet, ProductViewSet, SubCategoryViewSet


# Create your routers here.
products = (
    (r"categories", CategoryViewSet),
    (r"products", ProductViewSet),
    (r"subcategories", SubCategoryViewSet),
)
