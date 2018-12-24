from wtforms.widgets import HTMLString, html_params
from flask_admin.model.widgets import XEditableWidget
from jinja2 import escape


class ToggleInlineWidget(XEditableWidget):
    def __init__(self, fields, additional_kw=None):
        self._additional_kw = additional_kw if additional_kw is not None else {}
        self._fields = fields
        super(ToggleInlineWidget, self).__init__()

    def __call__(self, field, **kwargs):
        if field.name in self._fields:
            display_value = kwargs.pop('display_value', '')
            kwargs.setdefault('data-value', 1 if field.data else "")
            kwargs.setdefault('data-url', './ajax/update/')
            kwargs.setdefault('name', field.name)
            if not kwargs.get('pk'):
                raise Exception('pk required')
            kwargs['data-pk'] = str(kwargs.pop("pk"))
            kwargs['data-csrf'] = kwargs.pop("csrf", "")
            kwargs = self.get_kwargs(field, kwargs)
            kwargs['data-role'] = 'toggle-control'
            kwargs.update(self._additional_kw)
            return HTMLString(
                "<a {}>{}</a>".format(html_params(**kwargs), escape(display_value))
            )
        return super(ToggleInlineWidget, self).__call__(field, **kwargs)
