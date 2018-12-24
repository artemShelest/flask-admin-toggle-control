from flask import Flask, url_for, redirect
from flask_admin import Admin
from flask_admin._compat import iteritems
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_admin_toggle_control.toggle_control import ToggleInlineWidget

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    old_control = db.Column(db.Boolean)
    new_control = db.Column(db.Boolean)


class AdminView(ModelView):
    column_editable_list = ["old_control", "new_control"]

    extra_js = ["/static/admin/js/toggle-control.js"]

    def get_list_form(self):
        if self.form_args:
            validators = dict((key, {'validators': value["validators"]}) for key, value in
                              iteritems(self.form_args) if value.get("validators"))
        else:
            validators = None
        return self.scaffold_list_form(ToggleInlineWidget(("new_control",), {'class': "editable editable-click"}),
                                       validators)


@app.route("/")
@app.route("/index")
def index():
    return redirect(url_for("model.index_view"))


admin = Admin(app, name="Flask-Admin Toggle Control Example", template_mode="bootstrap3")
admin.add_view(AdminView(model=Model, session=db.session, name="Model", endpoint="model"))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
