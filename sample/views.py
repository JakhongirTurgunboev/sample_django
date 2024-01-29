from django.core import serializers
from django.http import JsonResponse, HttpResponse

from .models import Genre, Book, Author


def book_shop_view(request):
    if request.method == 'POST':
        book_name = request.POST.get('name')
        genre = request.POST.get('genre')
        genre = Genre.objects.get(pk=genre)
        published_year = request.POST.get('published_year')
        author = request.POST.get('author')
        author = Author.objects.get(pk=author)
        book = Book.objects.create(name=book_name,
                                   genre=genre,
                                   published_year=published_year,
                                   author=author,
                                   )
    authors = Author.objects.all()
    data = []
    for author in authors:
        author_data = {}
        author_data["name"] = author.first_name + ' ' + author.last_name
        books = Book.objects.filter(author=author).values_list('name', flat=True)
        author_data["books"] = list(books)
        data.append(author_data)
    return HttpResponse(data)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse(f"Book with id '{pk}' deleted")