# Book Management API

A simple FastAPI application for managing a list of books.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server with:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### GET /books
Returns a list of all books in JSON format.

### GET /books/{book_id}
Returns details of a single book by its ID. Returns 404 with "Book not found" message if the book doesn't exist.

## Example Requests

```bash
# Get all books
curl http://localhost:8000/books

# Get a specific book
curl http://localhost:8000/books/1
```

