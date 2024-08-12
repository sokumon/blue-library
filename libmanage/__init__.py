from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from libmanage.routes import root
from libmanage.routes import create
from libmanage.routes import read 
from libmanage.routes import update
from libmanage.routes import delete
from libmanage.routes import login
from libmanage.routes import search