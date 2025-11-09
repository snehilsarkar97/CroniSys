"""Database models using SQLAlchemy."""
from sqlalchemy import Column, Integer, String
from database.database import Base


class BookDB(Base):
    """Database model for Book table."""
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<BookDB(id={self.id}, title='{self.title}', author='{self.author}', year={self.year})>"

