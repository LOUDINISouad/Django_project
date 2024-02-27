from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
     path("hello", views.hello_world, name="hello"),
    path('add-book', views.add_book, name="book"),
    

] 