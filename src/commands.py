from flask.cli import with_appcontext
from src.models.book import Book
from src.ext import db
from src.enums import CoverType, Booktype, Audience
import click

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo('Initializing database...')
    db.drop_all()
    db.create_all()
    click.echo('Database initialized...')

@click.command("populate_db")
@with_appcontext
def populate_db(): #TODO ეს საერთოდ შესაცვლელია

    books = [
        {"title": "დიდი მოგზაურობა", "price": 32, "img": "book1.png"},
        {"title": "Amare La vita", "price": 31, "img": "book2.png"},
        {"title": "ქაოსიდან კოსმოსამდე", "price": 30, "img": "book3.png"},
        {"title": "იესეს ხის საკითხავები", "price": 29, "img": "book4.png"},
    ]

    for book in books:
        new_book = Book(
            title=book["title"],
            price=book["price"],
            image=book["img"],
            description="No description available",
            cover_type=CoverType.SOFT,
            book_type=Booktype.PRINT,
            audience=Audience.ADULT,
        )
        db.session.add(new_book)
    db.session.commit()
    click.echo('Database populated!')
