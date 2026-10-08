"""
SmartDog Backend – Configuration
"""
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./smartdog.db")
SECRET_KEY = os.getenv("SECRET_KEY", "smartdog-secret-key-for-dev-only-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 8  # 8 hours

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# CORS origins for local development
ALLOWED_ORIGINS = [
    "http://localhost:5173",   # Vite React dev server (Smart-Street-Dog)
    "http://localhost:3000",
    "http://127.0.0.1:5173",
    "http://localhost:8080",
    "http://localhost:8443",   # Current Vite port
    "null",                    # file:// origins for HTML5 admin dashboard
]

# AI Service connection (FastAPI Dog AI Server)
AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "http://localhost:8000")
