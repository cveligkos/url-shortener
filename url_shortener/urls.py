"""
URL configuration for url_shortener project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from url_shortener.redirect import link_redirect


urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("links/", include("links.urls")),
    re_path("^(?P<hash>[A-Za-z0-9]{5})$", link_redirect, name="link_redirect"),
]
