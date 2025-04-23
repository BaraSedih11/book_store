# Bazarcom Django Microservices Setup Guide

This guide will help you set up the Bazarcom e-commerce system built with Django and SQLite, following a microservices architecture. The system consists of four services:

1. Catalog Service - manages books and magazines inventory
2. Order Service - handles purchases
3. Gateway Service - acts as an API gateway
4. Frontend Service - provides a user interface

## Prerequisites

* Python 3.9 or higher
* pip (Python package manager)
* git (optional)

## Project Setup

1. Create Project Directory Structure

```bash
  mkdir book_store
  cd book_store
  mkdir catalog_service order_service gateway_service frontend_service
```

2. Set Up Virtual Environments (Option 1: Separate Environments)
Each service will use its own virtual environment:

#### For Windows:

```bash
  Catalog Service
  cd catalog_service
  python -m venv catalog_env
  catalog_env\Scripts\activate
  cd ..

  # Order Service
  cd order_service
  python -m venv order_env
  order_env\Scripts\activate
  cd ..
  
  # Gateway Service
  cd gateway_service
  python -m venv gateway_env
  gateway_env\Scripts\activate
  cd ..
  
  # Frontend Service
  cd frontend_service
  python -m venv frontend_env
  frontend_env\Scripts\activate
  cd ..
```

#### For macOS/Linux:
```bash
  Catalog Service
  cd catalog_service
  python -m venv catalog_env
  source catalog_env/bin/activate
  cd ..
  
  # Order Service
  cd order_service
  python -m venv order_env
  source order_env/bin/activate
  cd ..
  
  # Gateway Service
  cd gateway_service
  python -m venv gateway_env
  source gateway_env/bin/activate
  cd ..
  
  # Frontend Service
  cd frontend_service
  python -m venv frontend_env
  source frontend_env/bin/activate
  cd ..
```

3. Set Up Virtual Environments (Option 2: Single Environment)
Alternatively, you can use a single virtual environment for all services:

#### For Windows:
```bash
  python -m venv book_store_env
  book_store_env\Scripts\activate
```

#### For macOS/Linux:
```bash
  python -m venv bazarcom_env
  source bazarcom_env/bin/activate
```

Initialize and Migrate Database:

Running the Services
### Option 1: Running Services Individually
Open four separate terminal windows, one for each service:

Terminal 1 - Catalog Service:

```bash
cd catalog_service
# Activate the virtual environment if needed
python manage.py runserver 0.0.0.0:8000
```

Terminal 2 - Order Service:

```bash
cd order_service
# Activate the virtual environment if needed
python manage.py runserver 0.0.0.0:8001
```

Terminal 3 - Gateway Service:

```bash
cd gateway_service
# Activate the virtual environment if needed
python manage.py runserver 0.0.0.0:8002
```

Terminal 4 - Frontend Service:

```bash
cd frontend_service
# Activate the virtual environment if needed
python manage.py runserver 0.0.0.0:8003
```

### Option 2: Running with Docker Compose
If you have Docker and Docker Compose installed, you can run all services with a single command:

Run the services:

```bash
docker-compose up
```

This will build and start all services. The first build may take a few minutes.

### Accessing the Services
Once all services are running, you can access them at:

Frontend: http://localhost:8003
Gateway API: http://localhost:8002/gateway
Catalog API: http://localhost:8000/catalog
Order API: http://localhost:8001/order

### API Endpoints
#### Catalog Service

GET /catalog/books/ - Get all books
GET /catalog/magazines/ - Get all magazines
GET /catalog/books/<id>/ - Get book by ID
GET /catalog/books/topic/<topic>/ - Get books by topic
POST /catalog/books/<id>/decrement/ - Decrement book quantity (used by Order service)

#### Order Service

POST /order/purchase/<book_id>/ - Purchase a book

#### Gateway Service

GET /gateway/books/ - Get all books
GET /gateway/books/<id>/ - Get book by ID
GET /gateway/books/topic/<topic>/ - Get books by topic
POST /gateway/purchase/<book_id>/ - Purchase a book

#### Frontend Service

GET / - Home page
GET /books/ - View books page
GET /api/books/ - API endpoint that fetches books via Gateway

### Differences from Flask Implementation
This Django implementation differs from the original Flask version in several ways:

ORM Usage: Django's built-in ORM instead of SQLAlchemy
Project Structure: Django follows a project/app structure vs. Flask's more flexible approach
Admin Interface: Django provides a built-in admin interface
Template System: Django has its own template language
URL Routing: Django uses a different URL routing system
Serialization: Django REST Framework for serialization instead of Flask-Marshmallow

### Troubleshooting

Service Connection Issues: Make sure all services are running and the URL configurations are correct
CORS Issues: The CORS configuration allows all origins by default; modify if needed
Database Errors: Check migrations and ensure they're applied correctly
Docker Issues: Check Docker logs with docker-compose logs <service_name>

### Next Steps

Add authentication and user management
Implement more complex business logic
Add testing for each service
Enhance the frontend with more features
Add proper logging and monitoring
