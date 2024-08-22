from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Author(models.Model):
    fullname = models.CharField(max_length=50, null=False, unique=True)
    born_date = models.CharField(max_length=15, null=False)
    born_location = models.CharField(max_length=50, null=False)
    description = models.TextField()

    def __str__(self):
        return f'{self.fullname}'


class Quote(models.Model):
    quote = models.TextField(null=False)
    author = models.ForeignKey(Author, null=False, on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=50, blank=True))

    def __str__(self):
        return f'{self.quote}\n{self.author}.'

