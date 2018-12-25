from flask import Flask, url_for, redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import flask_admin_toggle_control as toggle_control
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    old_control = db.Column(db.Boolean)
    new_control = db.Column(db.Boolean)


class AdminView(toggle_control.ViewMixin, ModelView):
    column_editable_list = ["old_control", "new_control"]
    column_toggle_control_list = ["new_control"]


@app.route("/")
@app.route("/index")
def index():
    return redirect(url_for("model.index_view"))


admin = Admin(app, name="Flask-Admin Toggle Control Example", template_mode="bootstrap3")
admin.add_view(AdminView(model=Model, session=db.session, name="Model", endpoint="model"))
toggle_control.init_static_ep(app)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
