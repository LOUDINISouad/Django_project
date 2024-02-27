from django.shortcuts import render, HttpResponse
from MyLibrary.models import Book

from django.http import JsonResponse
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello there!")

def add_book(request):
    book = Book.objects.create(author="Oussamah", title="Bonjour")

    # Récupérer les détails du livre créé
    book_details = {
        'id': book.id,
        'title': book.title,
        'author': book.author
    }

    # Renvoyer les détails du livre sous forme de réponse JSON
    return JsonResponse(book_details)