from src.admin_views.base import SecureModelView
from flask_admin.form import FileUploadField
from src.config import Config
from markupsafe import Markup


class BookView(SecureModelView):
    column_list = (
        'title_ka',
        'title_en',
        'title_it',
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
            return Markup(f'<img src="/static/assets/{model.image}" width="100">')
        return ""

    column_formatters = {
        'description_ka': _description_formatter,
        'description_en': _description_formatter,
        'description_it': _description_formatter,
        'online_link': _link_formatter,
        'audio_link': _link_formatter,
        'android_link': _link_formatter,
        'ios_link': _link_formatter,
        'image': _image_formatter,
    }

    form_extra_fields = {
        'image': FileUploadField('Image', base_path=Config.UPLOAD_PATH)
    }

    form_columns = (
        'title_ka',
        'title_en',
        'title_it',
        'description_ka',
        'description_en',
        'description_it',
        'price',
        'image',
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
        'series',
    )

    can_create = True
    can_edit = True
    can_delete = True