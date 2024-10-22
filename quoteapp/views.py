import logging
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm
from .models import Quote, Author, PGAuthor, PGQuote
from django.contrib.auth.decorators import login_required
from collections import Counter


# Create your views here.
PERIOD = 10


def main(request):
    start = 0
    stop = PERIOD
    quotes = Quote.objects.all()[start:stop]
    next_page = '2'
    tags = top_tags(10)
    return render(request, 'quoteapp/index.html',
                  {'quotes': quotes,
                   'top_tags': tags,
                   'next_page': next_page,
                   'previous_page': None})


def page(request, page_number=1):
    start = PERIOD * (page_number - 1)
    stop = PERIOD * page_number
    quotes = Quote.objects.all()
    page_quotes = quotes[start:stop]
    number_of_pages = int(len(quotes)/PERIOD) + 1
    next_page = str(page_number + 1)
    previous_page = str(page_number - 1)
    if page_number == number_of_pages:
        next_page = None
    if page_number == 1:
        previous_page = None

    tags = top_tags(10)
    return render(request, 'quoteapp/index.html',
                  {'quotes': page_quotes,
                   'top_tags': tags,
                   'next_page': next_page,
                   'previous_page': previous_page})


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
    tags = top_tags(10)
    required_quotes = list()
    all_quotes = Quote.objects.all()
    for q in all_quotes:
        if tag in q.tags:
            required_quotes.append(q)
    return render(request, 'quoteapp/quotes_with_tag.html', context={'quotes': required_quotes,
                                                                     'top_tags': tags})


def top_tags(quantity):
    all_tags = list()
    all_quotes = Quote.objects.all()
    for q in all_quotes:
        for tag in q.tags:
            all_tags.append(tag)

    tag_counter = Counter(all_tags)
    most_common_tags = [tag[0] for tag in tag_counter.most_common(quantity)]

    return most_common_tags


@login_required()
def scrape_the_site(request):
    url = 'https://kind-sibbie-aleks-gmbh-38417f5e.koyeb.app/'
    print('scraping started')
    return render(request, 'quoteapp/scraping.html', context={'url': url})





