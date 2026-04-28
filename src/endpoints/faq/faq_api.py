from flask_restx import Resource, fields, reqparse
from src.ext import api
from src.models.faq import FrequentlyAskedQuestion

faq_model = api.model('FAQ', {
    "id": fields.Integer,
    "order_num": fields.Integer,
    "question": fields.String,
    "answer": fields.String,
})

parser = reqparse.RequestParser()
parser.add_argument('lang', required=False, type=str, choices=['ka', 'en', 'it'], default='ka')


def serialize_faq(f, lang='ka'):
    return {
        "id": f.id,
        "order_num": f.order_num,
        "question": f.get_question(lang),
        "answer": f.get_answer(lang),
    }


@api.route("/faq")
class FaqApi(Resource):
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        lang = args["lang"] or 'ka'
        faqs = FrequentlyAskedQuestion.query.order_by(FrequentlyAskedQuestion.order_num).all()
        return [serialize_faq(f, lang) for f in faqs]