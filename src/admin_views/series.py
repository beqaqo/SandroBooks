from src.admin_views.base import SecureModelView


class SeriesView(SecureModelView):
    column_list = ('title', 'description', 'books')

    form_columns = ('title', 'description')

    can_create = True
    can_edit = True
    can_delete = True