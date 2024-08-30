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


class PGAuthor(models.Model):
    fullname = models.CharField(max_length=100, null=False, unique=True)
    born_date = models.CharField(max_length=30, null=False)
    born_location = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return f'{self.fullname}'


class PGQuote(models.Model):
    quote = models.CharField(null=False, unique=True)
    author = models.ForeignKey(PGAuthor, on_delete=models.CASCADE, related_name='quotes')
    tags = ArrayField(models.CharField(max_length=50), blank=True, default=list)

    def __str__(self):
        return f'{self.quote}\n{self.author}.'

