"""firewall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', IndexView.as_view(), name='home'),
    re_path(r'^$', IndexView.as_view(), name='home'),
    path('available/', AvailableListView.as_view(), name='available'),
    path('rfca/', ReceivedFromCategoryListView.as_view(), name='rfca'),
    path('dtco/', DeliveryToCompanyListView.as_view(), name='dtco'),
    path('rfco/', ReceivedFromCompanyListView.as_view(), name='rfco'),
    path('dtca/', DeliveryToCategoryListView.as_view(), name='dtca'),
    path('search/', SearchView.as_view(), name="search"),
    path('export/', ExportView.as_view(), name="export"),
    re_path(r'^accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)