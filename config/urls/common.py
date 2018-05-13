# config/urls/common.py
"""bioservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin

from apps.core.routers import router

from rest_framework.documentation import include_docs_urls

API_TITLE = "bioservice"
API_DESCRIPTION = "..."

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(
        r"^api-auth/",
        include("rest_framework.urls", namespace="rest_framework")),
    url(
        r"^docs/",
        include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    url(r"^api/v1/", include(router.urls, namespace="api_v1")),
]
