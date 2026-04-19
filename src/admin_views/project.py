from src.admin_views.base import SecureModelView
from wtforms import FileField
from markupsafe import Markup

from src.ext import cloud


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

    def _on_model_change(self, form, model, is_created):
        if form.image.data and getattr(form.image.data, "filename", None):

            result = cloud.uploader.upload(
                form.image.data,
                folder="SandrosBooks"
            )

            model.image = result["secure_url"]
            model.image_public_id = result["public_id"]

        form.image.data = None


    column_formatters = {
        'image': _image_formatter
    }

    can_create = True
    can_edit = True
    can_delete = True