# Generated by Django 4.2.13 on 2024-05-21 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='client',
            table='user',
        ),
    ]
