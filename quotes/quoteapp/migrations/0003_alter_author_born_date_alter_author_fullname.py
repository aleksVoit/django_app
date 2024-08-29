# Generated by Django 5.1 on 2024-08-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quoteapp", "0002_rename_born_location_author_born_place"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="born_date",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="author",
            name="fullname",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]