# Generated by Django 4.2.1 on 2023-05-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstoread',
            name='book_description',
            field=models.TextField(default='SOME STRING', max_length=300),
        ),
    ]
