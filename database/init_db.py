"""Script to initialize the database with sample data."""
from database.database import init_db, SessionLocal
from database.models import BookDB


def init_sample_data():
    """Initialize database with sample book data."""
    # Create all tables
    init_db()
    
    # Create database session
    db = SessionLocal()
    
    try:
        # Check if books already exist
        existing_books = db.query(BookDB).count()
        if existing_books > 0:
            print(f"Database already contains {existing_books} books. Skipping sample data insertion.")
            return
        
        # Sample books data
        sample_books = [
            BookDB(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925),
            BookDB(title="To Kill a Mockingbird", author="Harper Lee", year=1960),
            BookDB(title="1984", author="George Orwell", year=1949),
            BookDB(title="Pride and Prejudice", author="Jane Austen", year=1813),
            BookDB(title="The Catcher in the Rye", author="J.D. Salinger", year=1951),
        ]
        
        # Add sample books to database
        for book in sample_books:
            db.add(book)
        
        db.commit()
        print(f"Successfully initialized database with {len(sample_books)} sample books.")
        
    except Exception as e:
        db.rollback()
        print(f"Error initializing database: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    init_sample_data()

