from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books, name='get_books'),
    path('books/<int:book_id>/', views.get_book_by_id, name='get_book_by_id'),
    path('books/topic/<str:topic>/', views.get_book_by_topic, name='get_book_by_topic'),
    path('purchase/<int:book_id>/', views.purchase_book, name='purchase_book'),
]