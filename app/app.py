import os

from flask import Flask

from . import db
from .views import views

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'tourdeflask.sqlite'),
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

db.init_app(app)


if __name__ == '__main__':
    app.run()
