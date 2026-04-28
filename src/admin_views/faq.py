from src.admin_views.base import SecureModelView


class FaqView(SecureModelView):
    column_list = ('order_num', 'question_ka', 'answer_ka')

    form_columns = (
        'order_num', 'question_ka', 'question_en', 'question_it', 'answer_ka', 'answer_en', 'answer_it',
    )

    can_create = True
    can_edit = True
    can_delete = True