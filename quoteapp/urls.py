from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),

    path('page/<int:page_number>', views.page, name='page'),

    path('author/', views.author, name='author'),
    path('quote/', views.quote, name='quote'),
    path('detail_quote/<str:quote_id>', views.detail_quote, name='detail_quote'),
    path('delete_quote/<str:quote_id>', views.delete_quote, name='delete_quote'),
    path('quotes_with_tag/<str:tag>', views.quotes_with_tag, name='quotes_with_tag'),
    path('detail_author/<str:author_name>', views.detail_author, name='detail_author'),
    path('delete_author/<str:author_id>', views.delete_author, name='delete_author'),
    path('scrape_the_site/', views.scrape_the_site, name='scrape_the_site'),

]
