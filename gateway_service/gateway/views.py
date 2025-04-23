import requests
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_books(request):
    response = requests.get(f"{settings.CATALOG_SERVICE_URL}/books/")
    if response.status_code == 200:
        return Response(response.json(), status=status.HTTP_200_OK)
    else:
        return Response({"message": "Error fetching books"}, status=response.status_code)

@api_view(['GET'])
def get_book_by_id(request, book_id):
    response = requests.get(f"{settings.CATALOG_SERVICE_URL}/books/{book_id}/")
    if response.status_code == 200:
        return Response(response.json(), status=status.HTTP_200_OK)
    else:
        return Response({"message": "Error fetching book"}, status=response.status_code)

@api_view(['GET'])
def get_book_by_topic(request, topic):
    response = requests.get(f"{settings.CATALOG_SERVICE_URL}/books/topic/{topic}/")
    if response.status_code == 200:
        return Response(response.json(), status=status.HTTP_200_OK)
    else:
        return Response({"message": "Error fetching books by topic"}, status=response.status_code)

@api_view(['POST'])
def purchase_book(request, book_id):
    response = requests.post(f"{settings.ORDER_SERVICE_URL}/purchase/{book_id}/")
    if response.status_code == 200:
        return Response(response.json(), status=status.HTTP_200_OK)
    else:
        return Response({"message": "Error processing purchase"}, status=response.status_code)
