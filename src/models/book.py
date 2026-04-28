from src.enums import CoverType, Booktype, Audience
from src.models.base import BaseModel
from src.ext import db

class Book(BaseModel):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)

    title_ka = db.Column(db.String, nullable=False)
    title_en = db.Column(db.String, nullable=False)
    title_it = db.Column(db.String, nullable=False)

    description_ka = db.Column(db.String, nullable=False)
    description_en = db.Column(db.String, nullable=False)
    description_it = db.Column(db.String, nullable=False)

    price = db.Column(db.Float)
    image = db.Column(db.String)
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

    def get_title(self, lang: str) -> str:
        return getattr(self, f"title_{lang}", self.title_ka)

    def get_description(self, lang: str) -> str:
        return getattr(self, f"description_{lang}", self.description_ka)
