from src.models.base import BaseModel
from src.ext import db


class Series(BaseModel):
    __tablename__ = 'series'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    books = db.relationship("Book", back_populates="series")

    def __repr__(self):
        return self.title