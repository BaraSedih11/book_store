from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Magazine
from .serializers import BookSerializer, MagazineSerializer

@api_view(['GET'])
def test_view(request):
    return Response({"message": "hello world"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_magazines(request):
    magazines = Magazine.objects.all()
    serializer = MagazineSerializer(magazines, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book_by_id(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response(
            {"message": "Book not found"},
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['GET'])
def get_book_by_topic(request, topic):
    books = Book.objects.filter(topic=topic)
    if not books:
        return Response(
            {"message": "No books found for the specified topic"},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def decrement_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        if book.quantity > 0:
            book.quantity -= 1
            book.save()
            return Response({
                "message": "Book decremented successfully",
                "book_id": book.id,
                "total_price": book.price
            })
        else:
            return Response(
                {"message": "Book out of stock"},
                status=status.HTTP_400_BAD_REQUEST
            )
    except Book.DoesNotExist:
        return Response(
            {"message": "Book not found"},
            status=status.HTTP_404_NOT_FOUND
        )