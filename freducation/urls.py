"""
URL configuration for freducation project.

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
import os
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from articles.sitemaps import articleSiteMap
from contact.sitemaps import contactSiteMap
from subscriber.sitemaps import subscribeSiteMap
from .views import (
    homeView,
    aboutView,
)

sitemaps = {'static': StaticViewSitemap,'articles': articleSiteMap,
            'contact': contactSiteMap,'subscribe': subscribeSiteMap}

urlpatterns = [
    path('', homeView,name='home'),
    path('about/', aboutView,name='about'),
    path('articles/',include('articles.urls')),
    path('contact/',include('contact.urls')),
    path('',include('subscriber.urls')),
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps},
    name="django.contrib.sitemaps.views.sitemap")
]

ADMIN_ENABLED = str(os.environ.get('ADMIN_ENABLED')) == "1"
if ADMIN_ENABLED:
    urlpatterns.append(path('admin/', admin.site.urls))

