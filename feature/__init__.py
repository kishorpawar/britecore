# flask imports
from flask import Flask

# SQLAlchemy impoorts
from flask_sqlalchemy import SQLAlchemy

# WSGI app object
app = Flask(__name__)

# Config
app.config.from_object('config')


# database object
db = SQLAlchemy(app)






# Build the database
#db.create_all()
