from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^generate_pdf/$', views.generate_pdf),
]
