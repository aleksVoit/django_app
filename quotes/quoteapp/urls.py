from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/', views.author, name='author'),
    path('quote/', views.quote, name='quote'),
    path('detail_quote/<int:quote_id>', views.detail_quote, name='detail_quote'),
    path('delete_quote/<int:quote_id>', views.delete_quote, name='delete_quote'),
]
