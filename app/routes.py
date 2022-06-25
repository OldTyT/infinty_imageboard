from flask import render_template, redirect, url_for
from app.models import *
from app import app, db
from app.forms import *
import sqlalchemy


@app.route('/', methods=['GET', 'POST'])
def index():
    form = add_post()
    posts = reversed(db.session.query(boardfinty).all())
    if form.validate_on_submit():
        db_form = boardfinty(post_txt=form.post_txt.data)
        db.session.add(db_form)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("board.html", posts=posts, form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
