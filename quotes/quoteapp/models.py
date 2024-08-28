from django.db import models
from django.contrib.postgres.fields import ArrayField

from mongoengine import Document, StringField, ReferenceField, ListField

# Create your models here.


class Author(Document):
    fullname = StringField(max_length=100, required=True, unique=True)
    born_date = StringField(max_length=30, required=True)
    born_location = StringField(max_length=100, required=True)
    description = StringField(required=True)

    def __str__(self):
        return f'{self.fullname}'


class Quote(Document):
    quote = StringField(required=True)
    author = ReferenceField(Author, required=True)
    tags = ListField()

    def __str__(self):
        return f'{self.quote}\n{self.author}.'

