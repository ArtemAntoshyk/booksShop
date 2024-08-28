from django.db import models
from django.urls import reverse


class Author(models.Model):
    author_name = models.CharField(max_length=150, unique=True, verbose_name='Author')

    class Meta:
        db_table = 'authors'
        verbose_name = 'Author'
        verbose_name_plural = 'Author'
        ordering = ("id",)

    def __str__(self):
        return self.author_name


class Books(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True, verbose_name="айді книги")
    name_book = models.CharField(max_length=150, unique=True, verbose_name='Назви книжок')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    page_amount = models.PositiveIntegerField(verbose_name='Кількість сторінок')
    year_production = models.PositiveIntegerField(verbose_name='Рік видання')
    description = models.CharField(verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    image = models.CharField( verbose_name="IMAGE", null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Author id")

    class Meta:
        db_table = 'books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ("id",)

    def __str__(self):
        return self.name_book

    def get_absolute_url(self):
        return reverse("books:book_detail", kwargs={"pk": self.pk})

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self, discount=10):
        if discount:
            return round(self.price - self.price * discount / 100, 2)
        return self.price


class Genres(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="айді жанру")
    genre_name = models.CharField(max_length=150, unique=True, verbose_name='Назва жанру')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'genres'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'
        ordering = ("id",)

    def __str__(self):
        return self.genre_name


class BooksAndTheirGenre(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='Книга')
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE, verbose_name='Жанр')

    class Meta:
        db_table = 'books_and_their_genre'
        verbose_name = 'Книга и её жанр'
        verbose_name_plural = 'Книги и их жанры'
        ordering = ("id",)

    def __str__(self):
        return f"{self.book.name_book} - {self.genre.genre_name}"
