from django.contrib import admin
from .models import Songs, Singer, Album, Genre, Book, Author
# Register your models here.
admin.site.register(Songs)
admin.site.register(Singer)
admin.site.register(Album)

admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Author)
