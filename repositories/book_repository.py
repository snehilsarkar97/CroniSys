"""Book repository - data access layer with database."""
from typing import List, Optional
from sqlalchemy.orm import Session
from models.book import Book, BookCreate, BookUpdate
from database.models import BookDB


class BookRepository:
    """Repository for managing book data with database."""
    
    def __init__(self, db: Session):
        """Initialize repository with database session."""
        self.db = db
    
    def get_all(self) -> List[Book]:
        """Get all books from database."""
        db_books = self.db.query(BookDB).all()
        return [self._db_to_model(book) for book in db_books]
    
    def get_by_id(self, book_id: int) -> Optional[Book]:
        """Get a book by its ID from database."""
        db_book = self.db.query(BookDB).filter(BookDB.id == book_id).first()
        if db_book:
            return self._db_to_model(db_book)
        return None
    
    def create(self, book_data: BookCreate) -> Book:
        """Create a new book in database."""
        db_book = BookDB(
            title=book_data.title,
            author=book_data.author,
            year=book_data.year
        )
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return self._db_to_model(db_book)
    
    def update(self, book_id: int, book_data: BookUpdate) -> Optional[Book]:
        """Update an existing book in database."""
        db_book = self.db.query(BookDB).filter(BookDB.id == book_id).first()
        if not db_book:
            return None
        
        # Update fields if provided
        if book_data.title is not None:
            db_book.title = book_data.title
        if book_data.author is not None:
            db_book.author = book_data.author
        if book_data.year is not None:
            db_book.year = book_data.year
        
        self.db.commit()
        self.db.refresh(db_book)
        return self._db_to_model(db_book)
    
    def delete(self, book_id: int) -> bool:
        """Delete a book by ID from database. Returns True if deleted, False if not found."""
        db_book = self.db.query(BookDB).filter(BookDB.id == book_id).first()
        if not db_book:
            return False
        
        self.db.delete(db_book)
        self.db.commit()
        return True
    
    @staticmethod
    def _db_to_model(db_book: BookDB) -> Book:
        """Convert database model to Pydantic model."""
        return Book(
            id=db_book.id,
            title=db_book.title,
            author=db_book.author,
            year=db_book.year
        )
