# Generated by Django 4.2.3 on 2023-08-22 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0015_bookcardsmodel_digital'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='phone_number',
            new_name='zipcode',
        ),
    ]
