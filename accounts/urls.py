from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/?$', views.login, name='accounts_login'),
    url(r'^logout/?$', views.logout, name='accounts_logout'),
]
