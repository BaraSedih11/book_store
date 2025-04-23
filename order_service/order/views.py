import requests
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

@api_view(['POST'])
def purchase_book(request, book_id):
    # Send request to catalog service to decrement book quantity
    response = requests.post(f"{settings.CATALOG_SERVICE_URL}/books/{book_id}/decrement/")
    
    if response.status_code == 200:
        response_data = response.json()
        
        # Create new order
        order = Order(
            book_id=book_id,
            total_price=response_data.get('total_price')
        )
        order.save()
        
        return Response(response_data.get('message'), status=status.HTTP_200_OK)
    else:
        return Response(
            {"message": "Error processing order", "details": response.json()},
            status=response.status_code
        )