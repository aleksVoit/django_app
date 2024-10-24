import django.template as template
from django.db.utils import IntegrityError

import requests
from bs4 import BeautifulSoup
from mongoengine import NotUniqueError
from ..models import PGAuthor, PGQuote

register = template.Library()


def parse_quotes(BASE_URL: str, this_page_url='/'):
    current_url = BASE_URL + this_page_url[:]
    response = requests.get(current_url)
    print(response.status_code)
    my_html = response.text
    soup = BeautifulSoup(my_html, 'lxml')
    quotes_info = soup.find_all('div', class_='bordered-div')
    for quote_info in quotes_info:
        quote = quote_info.find('span', class_='text').text
        author = quote_info.find('small', class_='author').text
        tags = quote_info.find_all('a', class_='tag')
        tags_ = list()
        for tag in tags:
            tags_.append(tag.text)

        authors_link = quote_info.find('a', class_='author')['href'].strip()
        parse_author(author, BASE_URL + authors_link)
        author_obj = PGAuthor.objects.filter(fullname=author).first()

        try:
            PGQuote(quote=quote, author=author_obj, tags=tags_).save()
        except NotUniqueError as err:
            print(f'{err}')
        except IntegrityError as err:
            print(f'{err}')

    next_page_tag = soup.find('li', class_='next')

    if next_page_tag:
        next_page_link = next_page_tag.find('a')['href']
        print(next_page_link)
        parse_quotes(BASE_URL, next_page_link)


def parse_author(author_name: str, author_url: str):
    response = requests.get(author_url)
    print(response.status_code)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    author_details = soup.find('div', class_='author-details')
    author_born_date = author_details.find('span', class_='author-born-date').text
    author_born_location = author_details.find('span', class_='author-born-location').text
    author_description = author_details.find('div', class_='author-description').text
    try:
        PGAuthor(fullname=author_name, born_date=author_born_date,
                 born_location=author_born_location, description=author_description).save()
    except NotUniqueError as err:
        print(f'{err}')
    except IntegrityError as err:
        print(f'{err}')


def scrape(base_url: str):
    url = base_url
    try:
        parse_quotes(url)
    except Exception as err:
        return err
    return 'The site was successfully scraped. All the data was saved to Database.'


register.filter('scrape_site', scrape)

