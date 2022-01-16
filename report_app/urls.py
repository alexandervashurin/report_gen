from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.admin.sites import site
from . import views

from django.views.static import serve

site.site_header = 'Информационная Система. Панель аналитика'
site.site_title = 'ИС'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
]