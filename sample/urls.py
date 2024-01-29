from django.urls import path

from .views import book_shop_view

urlpatterns = [
    path('', book_shop_view)
]