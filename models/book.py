"""Book model/schema definitions."""
from pydantic import BaseModel, Field
from typing import Optional


class Book(BaseModel):
    """Book model representing a book entity."""
    id: int
    title: str
    author: str
    year: int = Field(..., ge=1000, le=9999, description="Publication year")

    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "year": 1925
            }
        }


class BookCreate(BaseModel):
    """Schema for creating a new book (without ID)."""
    title: str
    author: str
    year: int = Field(..., ge=1000, le=9999, description="Publication year")

    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "year": 1925
            }
        }


class BookUpdate(BaseModel):
    """Schema for updating a book (all fields optional)."""
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = Field(None, ge=1000, le=9999, description="Publication year")


