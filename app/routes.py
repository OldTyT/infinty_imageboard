from flask import render_template
from app.models import *
from app import app, db
from app.forms import *
import sqlalchemy


@app.route('/')
@app.route('/index')
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
