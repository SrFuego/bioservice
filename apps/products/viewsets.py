# apps/products/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework import viewsets


# Local imports
from .models import Category, Product, SubCategory
from .serializers import (
    CategorySerializer, ProductSerializer, SubCategorySerializer)


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    lookup_field = "slug"


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    lookup_field = "slug"


class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subcategories to be viewed or edited.
    """
    queryset = SubCategory.objects.filter(is_active=True)
    serializer_class = SubCategorySerializer
    lookup_field = "slug"
