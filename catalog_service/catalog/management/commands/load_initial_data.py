from django.core.management.base import BaseCommand
from catalog.models import Book, Magazine

class Command(BaseCommand):
    help = 'Load initial data for books and magazines'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Book.objects.all().delete()
        Magazine.objects.all().delete()
        
        # Create books
        books = [
            Book(title='How to get a good grade in DOS in 40 minutes a day', 
                 topic="distributed_systems", price=10.99, quantity=100),
            Book(title='RPCs for Noobs', 
                 topic="distributed_systems", price=15.00, quantity=50),
            Book(title='Xen and the Art of Surviving Undergraduate School', 
                 topic="undergraduate_school", price=5.00, quantity=30),
            Book(title='Cooking for the Impatient Undergrad', 
                 topic="undergraduate_school", price=10.00, quantity=70),
        ]
        Book.objects.bulk_create(books)
        self.stdout.write(self.style.SUCCESS(f'Created {len(books)} books'))
        
        # Create magazines
        magazines = [
            Magazine(title='National Geographic', price=5.99, quantity=50),
            Magazine(title='Time', price=4.99, quantity=30),
            Magazine(title='Vogue', price=6.99, quantity=20),
            Magazine(title='Forbes', price=7.99, quantity=15),
        ]
        Magazine.objects.bulk_create(magazines)
        self.stdout.write(self.style.SUCCESS(f'Created {len(magazines)} magazines'))
