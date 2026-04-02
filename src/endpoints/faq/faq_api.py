from flask_restx import Resource, fields
from src.ext import api
from src.models.faq import FrequentlyAskedQuestion

faq_model = api.model('FAQ', {
    "id": fields.Integer,
    "order_num": fields.Integer,
    "question": fields.String,
    "answer": fields.String,
})


@api.route("/faq")
class FaqApi(Resource):
    @api.marshal_list_with(faq_model)
    def get(self):
        faqs = FrequentlyAskedQuestion.query.order_by(FrequentlyAskedQuestion.order_num).all()
        return faqs