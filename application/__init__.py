from decouple import config
from flask import Flask
from flask_migrate import Migrate

from application.db import db
from application.models import Entry

app = Flask(__name__)
app.config["SECRET_KEY"] = config("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}' \
                                              f'@localhost:{config("DB_PORT")}/{config("DB_NAME")}'
migrate = Migrate(app, db)
db.init_app(app)

from application import routes
