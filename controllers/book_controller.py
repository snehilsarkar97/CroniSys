"""Book controller - handles HTTP requests for books."""
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from sqlalchemy.orm import Session
from models.book import Book, BookCreate, BookUpdate
from repositories.book_repository import BookRepository
from database.database import get_db

# Create router for book endpoints
router = APIRouter(prefix="/books", tags=["books"])


@router.get("", response_model=List[Book])
async def get_books(db: Session = Depends(get_db)):
    """Return a list of all books."""
    repository = BookRepository(db)
    return repository.get_all()


@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    """Return details of a single book by its ID."""
    repository = BookRepository(db)
    book = repository.get_by_id(book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return book


@router.post("", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BookCreate, db: Session = Depends(get_db)):
    """Create a new book."""
    repository = BookRepository(db)
    return repository.create(book_data)


@router.put("/{book_id}", response_model=Book)
async def update_book(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db)):
    """Update an existing book."""
    repository = BookRepository(db)
    book = repository.update(book_id, book_data)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return book


@router.delete("/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book by ID."""
    repository = BookRepository(db)
    deleted = repository.delete(book_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return {"message": "Book successfully deleted"}
