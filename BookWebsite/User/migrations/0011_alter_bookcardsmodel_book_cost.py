# Generated by Django 4.2.3 on 2023-07-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_remove_order_book_alter_order_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcardsmodel',
            name='book_cost',
            field=models.IntegerField(default=0),
        ),
    ]
