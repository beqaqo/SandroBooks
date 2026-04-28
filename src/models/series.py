from src.models.base import BaseModel
from src.ext import db


class Series(BaseModel):
    __tablename__ = 'series'

    id = db.Column(db.Integer, primary_key=True)
    title_ka = db.Column(db.String, nullable=False)
    title_en = db.Column(db.String, nullable=False)
    title_it = db.Column(db.String, nullable=False)
    description_ka = db.Column(db.Text, nullable=False)
    description_en = db.Column(db.Text, nullable=False)
    description_it = db.Column(db.Text, nullable=False)
    books = db.relationship("Book", back_populates="series")

    def __repr__(self):
        return self.title_ka

    def get_title(self, lang: str) -> str:
        return getattr(self, f"title_{lang}", self.title_ka)

    def get_description(self, lang: str) -> str:
        return getattr(self, f"description_{lang}", self.description_ka)