from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('brand',views.brand,name="brand"),
    path('special',views.special,name="special"),
    path('contact',views.contact,name="contact"),
    
]