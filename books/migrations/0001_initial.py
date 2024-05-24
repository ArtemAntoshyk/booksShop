# Generated by Django 4.2.13 on 2024-05-21 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='айді жанру')),
                ('name_book', models.CharField(max_length=150, unique=True, verbose_name='Назви книжок')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('page_amount', models.PositiveIntegerField(verbose_name='Кількість сторінок')),
                ('year_production', models.PositiveIntegerField(verbose_name='Рік видання')),
                ('description', models.CharField(verbose_name='Опис')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'db_table': 'books',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='айді жанру')),
                ('genre_name', models.CharField(max_length=150, unique=True, verbose_name='Назва жанру')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанри',
                'db_table': 'genres',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='BooksAndTheirGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books', verbose_name='Книга')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.genres', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Книга и её жанр',
                'verbose_name_plural': 'Книги и их жанры',
                'db_table': 'books_and_their_genre',
                'ordering': ('id',),
            },
        ),
    ]
