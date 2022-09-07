from flask import Flask
from .site.routes import site
from .authentication.routes import auth
from .bookshelves.routes import shelves 
from config import Config


app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(shelves)
app.register_blueprint(auth)
app.config.from_object(Config)