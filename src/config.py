from os import path, environ

class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))

    DATABASE_URL = environ.get("DATABASE_URL")
    if DATABASE_URL:
        # Fix Render postgres:// issue
        if DATABASE_URL.startswith("postgres://"):
            DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        # fallback for local development
        SQLALCHEMY_DATABASE_URI = "sqlite:///books.db"

    SECRET_KEY = environ.get("SECRET_KEY", "defaultsecretkey")
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "assets")

    CLOUDINARY_CLOUD_NAME = environ.get("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY = environ.get("CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET = environ.get("CLOUDINARY_API_SECRET")