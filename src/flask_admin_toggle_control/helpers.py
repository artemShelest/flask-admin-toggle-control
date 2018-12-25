import os

from flask import send_from_directory

_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
JS_FILE_NAME = "toggle-control.js"
JS_PATH = "/static/admin/js/" + JS_FILE_NAME


def _serve_js():
    return send_from_directory(_DIR, JS_FILE_NAME)


def init_static_ep(app, ep="toggle_control_static"):
    app.add_url_rule(JS_PATH, ep, _serve_js)
