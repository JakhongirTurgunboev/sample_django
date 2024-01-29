from django.core import serializers
from django.http import JsonResponse, HttpResponse

from .models import Genre, Book, Author


def book_shop_view(request):
    authors = Author.objects.all()
    data = []
    for author in authors:
        author_data = {}
        author_data["name"] = author.first_name + ' ' + author.last_name
        books = Book.objects.filter(author=author).values_list('name', flat=True)
        author_data["books"] = list(books)
        data.append(author_data)
    return HttpResponse(data)
