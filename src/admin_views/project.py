from src.admin_views.base import SecureModelView
from wtforms import FileField
from markupsafe import Markup


class ProjectsView(SecureModelView):
    column_list = ('title', 'description', 'link', 'image')

    form_columns = ('title', 'description', 'link', 'image')

    form_extra_fields = {
        'image': FileField('Image')
    }

    def _image_formatter(self, context, model, name):
        if model.image:
            return Markup(f'<img src="{model.image}" width="100">')
        return ""

    column_formatters = {
        'image': _image_formatter
    }

    can_create = True
    can_edit = True
    can_delete = True