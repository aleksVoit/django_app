import json

from django.shortcuts import render, redirect
from .forms import AuthorForm, QuoteForm
from .models import Quote

# Create your views here.


def main(request):
    return render(request, 'quoteapp/index.html')


def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/author.html', {'form': form})
    return render(request, 'quoteapp/author.html', {'form': AuthorForm()})


def quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        elif 'author' in form.errors and 'The author does not exist.' in form.errors['author']:
            return render(request, 'quoteapp/author.html', {'form': AuthorForm, 'add_quote': True})
        else:
            return render(request, 'quoteapp/quote.html', {'form': form})
    return render(request, 'quoteapp/quote.html', {'form': QuoteForm()})


