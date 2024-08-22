# Generated by Django 5.1 on 2024-08-21 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quoteapp", "0002_alter_quote_author_alter_quote_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quote",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="quoteapp.author"
            ),
        ),
    ]