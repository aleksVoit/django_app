from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm
from .models import Quote, Author
from django.contrib.auth.decorators import login_required

# Create your views here.


def main(request):
    quotes = Quote.objects.all()
    print(request.body)
    return render(request, 'quoteapp/index.html', {'quotes': quotes})


@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return_to_quote = request.session.get('return_to_quote', None)
            if return_to_quote:
                return redirect(to='quoteapp:quote')
            else:
                return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/author.html', {'form': form})
    return render(request, 'quoteapp/author.html', {'form': AuthorForm()})


@login_required
def quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        elif 'The author does not exist.' in form.errors['author']:
            request.session['return_to_quote'] = request.POST
            return redirect('quoteapp:author')
        elif 'author' in form.errors:
            return render(request, 'quoteapp/author.html', {'form': AuthorForm})
        else:
            return render(request, 'quoteapp/quote.html', {'form': form})
    else:
        quote_data = request.session.pop('return_to_quote', None)
        form = QuoteForm(quote_data) if quote_data else QuoteForm()
        return render(request, 'quoteapp/quote.html', {'form': form})


def detail_quote(request, quote_id):
    d_quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quoteapp/detail_quote.html', {'quote': d_quote})


def delete_quote(request, quote_id):
    if request.user.is_authenticated:
        Quote.objects.get(pk=quote_id).delete()
    return redirect(to='quoteapp:main')


def detail_author(request, author_id):
    d_author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quoteapp/detail_author.html', {'d_author': d_author})


def delete_author(request, author_id):
    if request.user.is_authenticated:
        Author.objects.get(pk=author_id).delete()
    return redirect(to='quoteapp:main')

