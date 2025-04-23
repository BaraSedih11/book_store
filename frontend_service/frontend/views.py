import requests
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'frontend/index.html')

def books(request):
    try:
        # Get books from gateway service
        response = requests.get(f"{settings.GATEWAY_SERVICE_URL}/books/")
        books = response.json()
        return render(request, 'frontend/books.html', {'books': books})
    except Exception as e:
        return render(request, 'frontend/books.html', {'error': str(e)})

def api_books(request):
    try:
        # Get books from gateway service
        response = requests.get(f"{settings.GATEWAY_SERVICE_URL}/books/")
        return JsonResponse(response.json(), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)