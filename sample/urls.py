from django.urls import path

from .views import book_shop_view, delete_book

urlpatterns = [
    path('', book_shop_view),
    path('<int:pk>/', delete_book)
]