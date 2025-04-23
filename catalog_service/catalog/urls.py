from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_view, name='test'),
    path('books/', views.get_books, name='get_books'),
    path('magazines/', views.get_magazines, name='get_magazines'),
    path('books/<int:book_id>/', views.get_book_by_id, name='get_book_by_id'),
    path('books/topic/<str:topic>/', views.get_book_by_topic, name='get_book_by_topic'),
    path('books/<int:book_id>/decrement/', views.decrement_book, name='decrement_book'),
]