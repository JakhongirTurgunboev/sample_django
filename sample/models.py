from django.db import models

# Create your models here.


class Singer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Album(models.Model):
    CHOICES = (
        ("C", "Classic"),
        ("P", "Pop"),
        ("R", "Rock"),
        ("J", "Jazz")
    )
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=1, choices=CHOICES, default='C')
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Songs(models.Model):
    name = models.CharField(max_length=50)
    length_in_seconds = models.PositiveIntegerField(default=1)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now_add=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    published_year = models.PositiveIntegerField(default=2024)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


