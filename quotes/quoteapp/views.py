from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm
from .models import Quote, Author

# Create your views here.


def main(request):
    quotes = Quote.objects.all()
    return render(request, 'quoteapp/index.html', {'quotes': quotes})


def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id).delete()
    return redirect(to='quoteapp:main')


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

