"""Main application file for Book Management API."""
from fastapi import FastAPI
from controllers.book_controller import router as book_router
from database.database import init_db

# Create FastAPI application
app = FastAPI(title="Book Management API")

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    """Initialize database tables on application startup."""
    init_db()

# Register routes
app.include_router(book_router)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the Book Management API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
