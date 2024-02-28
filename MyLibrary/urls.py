from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("hello", views.hello_world, name="hello"),
    path('add-book', views.add_book, name="add_book"),
    #path("books/<int:id>", views.get_book_by_id, name="get_book_by_id"),
    #path("books/<int:id>/delete", views.delete, name="delete_book"),
    path("books/<int:id>", views.get_book_by_id, name="get_book_by_id")
]
    

