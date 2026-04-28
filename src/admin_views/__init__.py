from src.admin_views.book import BookView
from src.admin_views.series import SeriesView
from src.admin_views.project import ProjectsView
from src.admin_views.faq import FaqView

def register_admin_views(admin, db):
    from src.models.book import Book
    from src.models.series import Series
    from src.models.project import Project
    from src.models.faq import FrequentlyAskedQuestion
    admin.add_view(BookView(Book, db.session, name="Books Default", endpoint="books_default"))
    admin.add_view(SeriesView(Series, db.session))
    admin.add_view(ProjectsView(Project, db.session))
    admin.add_view(FaqView(FrequentlyAskedQuestion, db.session, name="FAQ"))