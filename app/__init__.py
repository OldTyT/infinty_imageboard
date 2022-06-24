from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
from app import routes, models
migrate = Migrate(app, db)
#app.run(host="127.0.0.1", port="5000", debug=True)