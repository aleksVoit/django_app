from mongo_connect import connect
from mongo_models import Quote, Author


if __name__ == '__main__':
    quote = Quote.objects.first()
    author = Author.objects(fullname=quote.author).first()
    print(quote.tags, quote.quote, quote.author)
    print(author.fullname, author.born_date, author.born_location, author.description)

