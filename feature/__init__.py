# flask imports
from flask import Flask

# SQLAlchemy impoorts
from flask_sqlalchemy import SQLAlchemy

#migrate imports
from flask_migrate import Migrate
# WSGI app object
app = Flask(__name__)

# Config
app.config.from_object('config')


# database object
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from feature import models




# Build the database
db.create_all()
