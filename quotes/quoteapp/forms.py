from django.forms import ModelForm, CharField, TextInput, Textarea
from .models import Author


class AuthorForm(ModelForm):
    fullname = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    born_date = CharField(min_length=5, max_length=15, required=True, widget=TextInput())
    born_location = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    description = CharField(widget=Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
