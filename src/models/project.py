from src.models.base import BaseModel
from src.ext import db


class Project(BaseModel):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(128), nullable=True)
    image = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return self.title