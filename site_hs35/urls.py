from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
   path('', views.home_page, name='home'),
   path('', views.for_pupils, name='pupils'),
   path('', views.for_teachers, name='teachers'),
   path('', views.for_parents, name='parents'),
]   
