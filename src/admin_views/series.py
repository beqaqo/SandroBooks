from src.admin_views.base import SecureModelView


class SeriesView(SecureModelView):
    column_list = ('title_ka', 'title_en', 'title_it', 'books')

    form_columns = (
        'title_ka', 'title_en', 'title_it',
        'description_ka', 'description_en', 'description_it',
    )

    can_create = True
    can_edit = True
    can_delete = True