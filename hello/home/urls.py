from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about', views.about , name='about'),
    path('contact', views.contact , name='contact'),
    path('skill', views.skill , name='skill')
]
