from flask_restx import Resource, fields, reqparse
from src.ext import api
from src.models.book import Book
from src.enums import CoverType, Booktype, Audience
import random

book_model = api.model('Book', {"id": fields.Integer, "title": fields.String, "image": fields.String})

book_detail_model = api.model('BookDetail', {
    "id": fields.Integer,
    "title": fields.String,
    "image": fields.String,
    "price": fields.Float,
    "description": fields.String,
    "publication_year": fields.Integer,
    "page_count": fields.Integer,
    "format": fields.String,
    "ISBN": fields.Integer,
    "cover_type": fields.String,
    "book_type": fields.String,
    "audience": fields.String,
    "online_link": fields.String,
    "audio_link": fields.String,
    "android_link": fields.String,
    "ios_link": fields.String,
    "about_series": fields.String,
})

parser = reqparse.RequestParser()
parser.add_argument('cover_type', type=str, choices=[e.value for e in CoverType], required=False)
parser.add_argument("audience", type=str, choices=[e.value for e in Audience], required=False)
parser.add_argument("book_type", type=str, choices=[e.value for e in Booktype], required=False)
parser.add_argument("search", type=str, required=False)
parser.add_argument("sort", type=str, required=False)
parser.add_argument("page", type=int, required=False, default=1)
parser.add_argument("page_size", type=int, required=False, default=12)


def serialize_book(b):
    return {"id": b.id, "title": b.title, "image": b.image}


def serialize_book_detail(b):
    return {
        "id": b.id,
        "title": b.title,
        "image": b.image,
        "price": b.price,
        "description": b.description,
        "publication_year": b.publication_year,
        "page_count": b.page_count,
        "format": b.format,
        "ISBN": b.ISBN,
        "cover_type": b.cover_type.value if b.cover_type else None,
        "book_type": b.book_type.value if b.book_type else None,
        "audience": b.audience.value if b.audience else None,
        "online_link": b.online_link,
        "audio_link": b.audio_link,
        "android_link": b.android_link,
        "ios_link": b.ios_link,
        "about_series": b.about_series,
    }


@api.route("/books")
class BooksApi(Resource):
    def get(self):
        args = parser.parse_args()

        page_size = max(1, min(args["page_size"] or 12, 48))
        page = max(1, args["page"] or 1)

        query = (Book
                 .query)

        if args["audience"]:
            query = query.filter(Book.audience == args["audience"])
        if args["book_type"]:
            query = query.filter(Book.book_type == args["book_type"])
        if args["cover_type"]:
            query = query.filter(Book.cover_type == args["cover_type"])
        if args["search"]:
            query = query.filter(Book.title.ilike(f"%{args['search']}%"))

        sort = args.get("sort")
        if sort == "free":
            query = query.filter(Book.price == 0)
        elif sort == "price_desc":
            query = query.order_by(Book.price.desc())
        elif sort == "price_asc":
            query = query.order_by(Book.price.asc())
        elif sort == "date_desc":
            query = query.order_by(Book.publication_year.desc())
        elif sort == "date_asc":
            query = query.order_by(Book.publication_year.asc())

        total = query.count()
        pages = (total + page_size - 1) // page_size
        books = query.offset((page - 1) * page_size).limit(page_size).all()

        return {
            "items": [serialize_book(b) for b in books],
            "total": total,
            "page": page,
            "page_size": page_size,
            "pages": pages,
        }


@api.route("/book/<int:id>")
class BookApi(Resource):
    def get(self, id):
        book = Book.query.get_or_404(id)

        same_series = []
        if book.about_series:
            same_series_query = (
                Book.query
                .filter(Book.about_series == book.about_series, Book.id != id)
                .limit(4)
                .all()
            )
            same_series = [serialize_book(b) for b in same_series_query]

        excluded_ids = {id} | {b["id"] for b in same_series}
        other_books = Book.query.filter(~Book.id.in_(excluded_ids)).all()
        you_may_also_like = [serialize_book(b) for b in random.sample(other_books, min(4, len(other_books)))]

        return {
            "book": serialize_book_detail(book),
            "you_may_also_like": you_may_also_like,
            "same_series": same_series,
        }