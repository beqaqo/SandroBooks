from src.admin_views.base import SecureModelView
from flask_admin.form import FileUploadField
from src.config import Config
from markupsafe import Markup


class ProjectsView(SecureModelView):
    column_list = ('title_ka', 'title_en', 'title_it', 'link', 'image')

    form_columns = (
        'title_ka', 'title_en', 'title_it',
        'description_ka', 'description_en', 'description_it',
        'link', 'image'
    )

    form_extra_fields = {
        'image': FileUploadField('Image', base_path=Config.UPLOAD_PATH)
    }

    def _image_formatter(self, context, model, name):
        if model.image:
            return Markup(f'<img src="/static/assets/{model.image}" width="100">')
        return ""

    column_formatters = {
        'image': _image_formatter
    }

    can_create = True
    can_edit = True
    can_delete = True