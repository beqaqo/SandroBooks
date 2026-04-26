from src.models.base import BaseModel
from src.ext import db


class Project(BaseModel):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title_ka = db.Column(db.String(128), nullable=False)
    title_en = db.Column(db.String(128), nullable=False)
    title_it = db.Column(db.String(128), nullable=False)
    description_ka = db.Column(db.Text, nullable=False)
    description_en = db.Column(db.Text, nullable=False)
    description_it = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(128), nullable=True)
    image = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return self.title_ka

    def get_title(self, lang: str) -> str:
        return getattr(self, f"title_{lang}", self.title_ka)

    def get_description(self, lang: str) -> str:
        return getattr(self, f"description_{lang}", self.description_ka)