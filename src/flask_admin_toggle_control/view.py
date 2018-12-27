from flask_admin._compat import iteritems

from .helpers import JS_PATH
from .widget import ToggleInlineWidget


class ViewMixin(object):
    column_toggle_control_list = []
    extra_js = [JS_PATH]
    toggle_control_options = {'class': "editable editable-click"}

    def get_list_form(self):
        if self.form_args:
            validators = dict((key, {'validators': value["validators"]}) for key, value in
                              iteritems(self.form_args) if value.get("validators"))
        else:
            validators = None
        return self.scaffold_list_form(
            ToggleInlineWidget(self.column_toggle_control_list, self.toggle_control_options), validators)
