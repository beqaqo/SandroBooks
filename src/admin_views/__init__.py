from src.admin_views.book import BookView
from src.admin_views.series import SeriesView

def register_admin_views(admin, db):
    from src.models.book import Book
    from src.models.series import Series
    admin.add_view(BookView(Book, db.session))
    admin.add_view(SeriesView(Series, db.session))