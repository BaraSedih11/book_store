from django.urls import path
from . import views

urlpatterns = [
    path('purchase/<int:book_id>/', views.purchase_book, name='purchase_book'),
]