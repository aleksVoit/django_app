# Generated by Django 5.1 on 2024-08-25 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quoteapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="author",
            old_name="born_location",
            new_name="born_place",
        ),
    ]
