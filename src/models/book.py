from src.enums import CoverType, Booktype, Audience
from src.models.base import BaseModel
from src.ext import db

class Book(BaseModel):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Float)
    image = db.Column(db.String)
    description = db.Column(db.String, nullable=False)
    publication_year = db.Column(db.Integer)
    page_count = db.Column(db.Integer)
    format = db.Column(db.String)
    ISBN = db.Column(db.Integer)
    cover_type = db.Column(db.Enum(CoverType), nullable=False)
    book_type = db.Column(db.Enum(Booktype), nullable=False)
    audience = db.Column(db.Enum(Audience), nullable=False)
    online_link = db.Column(db.String)
    audio_link = db.Column(db.String)
    android_link = db.Column(db.String)
    ios_link = db.Column(db.String)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=True)
    series = db.relationship("Series", back_populates="books")
