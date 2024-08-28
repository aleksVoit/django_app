import logging
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm
from .models import Quote, Author
from django.contrib.auth.decorators import login_required


# Create your views here.


def main(request):
    quotes = Quote.objects.all()
    return render(request, 'quoteapp/index.html', {'quotes': quotes})


@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            Author(fullname=form.cleaned_data['fullname'],
                   born_date=form.cleaned_data['born_date'],
                   born_location=form.cleaned_data['born_location'],
                   description=form.cleaned_data['description']).save()
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

            author_name = form.cleaned_data['author']
            add_author = Author.objects(fullname=str(author_name)).first()

            Quote(
                quote=form.cleaned_data['quote'],
                author=add_author.id,
                tags=form.cleaned_data['tags']
            ).save()
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
    try:
        d_quote = Quote.objects(id=quote_id).first()
        return render(request, 'quoteapp/detail_quote.html', {'quote': d_quote})
    except IOError as err:
        print(f'{err}')


def delete_quote(request, quote_id):
    if request.user.is_authenticated:
        Quote.objects(id=quote_id).delete()
    return redirect(to='quoteapp:main')


def detail_author(request, author_name: str):
    try:
        d_author = Author.objects(fullname=author_name).first()
        return render(request, 'quoteapp/detail_author.html', {'d_author': d_author})
    except IOError as err:
        logging.debug(f'{err}')


def delete_author(request, author_id):
    if request.user.is_authenticated:
        del_author = Author.objects(id=author_id).first()
        del_quotes = Quote.objects(author=author_id).all()
        del_author.delete()
        del_quotes.delete()
    return redirect(to='quoteapp:main')


def quotes_with_tag(request, tag):
    print(tag)
    return render(request, 'quoteapp:quotes_with_tag')

