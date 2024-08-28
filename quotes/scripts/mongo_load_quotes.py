# mongo_to_postgres.py
import os
import sys
import django
from mongo_connect import connect
from mongo_models import Quote as MG_Quote, Author as MG_Author

# Настройка Django
sys.path.append('/Users/aleksandr.voitushenko/Desktop/GoIT/PythonWeb24/django_app/quotes')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')
django.setup()

from quoteapp.models import Author, Quote


def migrate_authors():
    mongo_authors = MG_Author.objects.all()

    for mongo_author in mongo_authors:
        # Проверка, существует ли автор в PostgreSQL
        if not Author.objects.filter(fullname=mongo_author['fullname']).exists():
            Author.objects.create(
                fullname=mongo_author['fullname'],
                born_date=mongo_author['born_date'],
                born_location=mongo_author['born_location'],
                description=mongo_author['description']
            )


def migrate_quotes():
    mongo_quotes = MG_Quote.objects.all()

    for mongo_quote in mongo_quotes:
        author = Author.objects.filter(fullname=mongo_quote['author']).first()
        if author and not Quote.objects.filter(quote=mongo_quote['quote']).exists():
            Quote.objects.create(
                quote=mongo_quote['quote'],
                author=author,
                tags=mongo_quote['tags']
            )


if __name__ == '__main__':
    migrate_authors()
    migrate_quotes()
