from src.admin_views.base import SecureModelView
from wtforms import FileField
from markupsafe import Markup

from src.ext import cloud, uploader


class BookView(SecureModelView):
    column_list = (
        'title',
        'description',
        'image',
        'page_count',
        'online_link',
        'audio_link',
        'android_link',
        'ios_link',
    )

    def _description_formatter(self, view, model, name):
        desc = getattr(model, name) or ""
        return desc[:100] + ('...' if len(desc) > 100 else '')

    def _link_formatter(self, view, model, name):
        url = getattr(model, name)
        if url:
            return Markup(f'<a href="{url}" target="_blank">View</a>')
        return ""

    def _image_formatter(self, context, model, name):
        if model.image:
            return Markup(f'<img src="{model.image}" width="100">')
        return ""

    def _on_model_change(self, form, model, is_created):
        if form.image.data:
            result = cloud.uploader.upload(form.image.data, folder="SandrosBooks", public_id=f"book_{model.id}")
            model.image = result["secure_url"]
            form.image.data = None

    def on_model_delete(self, model):
        if model.image_public_id:
            cloud.uploader.destroy(f"book_{model.id}")

    column_formatters = {
        'description': _description_formatter,
        'online_link': _link_formatter,
        'audio_link': _link_formatter,
        'android_link': _link_formatter,
        'ios_link': _link_formatter,
        'image': _image_formatter,
    }

    form_extra_fields = {
        'image': FileField('Image')
    }

    form_columns = (
        'title',
        'price',
        'image',
        'description',
        'publication_year',
        'page_count',
        'format',
        'ISBN',
        'cover_type',
        'book_type',
        'audience',
        'online_link',
        'audio_link',
        'android_link',
        'ios_link',
        'series'
    )

    can_create = True
    can_edit = True
    can_delete = True