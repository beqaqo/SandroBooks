from src.models.base import BaseModel
from src.ext import db


class FrequentlyAskedQuestion(BaseModel):
    __tablename__ = "faqs"

    id = db.Column(db.Integer, primary_key=True)
    order_num = db.Column(db.Integer, nullable=False, default=0)
    question_ka = db.Column(db.String, nullable=False)
    question_en = db.Column(db.String, nullable=False)
    question_it = db.Column(db.String, nullable=False)
    answer_ka = db.Column(db.String, nullable=False)
    answer_en = db.Column(db.String, nullable=False)
    answer_it = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<FAQ #{self.order_num}: {self.question_ka[:50]}>"

    def get_question(self, lang: str) -> str:
        return getattr(self, f"question_{lang}", self.question_ka)

    def get_answer(self, lang: str) -> str:
        return getattr(self, f"answer_{lang}", self.answer_ka)