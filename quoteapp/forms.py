import os
import sys
from django import setup

from django.forms import CharField, TextInput, Textarea, ValidationError, Form
from .models import Author, Quote


class AuthorForm(Form):
    fullname = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    born_date = CharField(min_length=5, max_length=15, required=True, widget=TextInput())
    born_location = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    description = CharField(widget=Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(Form):
    quote = CharField(widget=Textarea(attrs={'rows': 2, 'cols': 40}))
    author = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    tags = CharField(widget=Textarea(attrs={'rows': 1, 'cols': 50}), help_text='Enter the tags separated by commas')

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']

    def clean_author(self):
        author_name = self.cleaned_data['author']
        if not Author.objects(fullname=author_name):
            raise ValidationError("The author does not exist.")
        return Author.objects(fullname=author_name).first()

    def clean_tags(self):
        data = self.cleaned_data['tags']
        tags_list = [tag.strip() for tag in data.split(',') if tag.strip()]
        return tags_list
