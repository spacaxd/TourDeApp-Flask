from flask import Blueprint

views = Blueprint(__name__, "views")


@views.route('/')
def hello_world():  # put application's code here
    return "render_template(index.html)"
