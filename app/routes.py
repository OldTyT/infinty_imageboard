from flask import render_template, redirect, url_for, request
from app.models import *
from app import app, db, api
from app.forms import *
from flask_json import as_json
from flask_restful import Resource, Api

api_v = "v1"


class posts_api(Resource):
    def get(self):
        data = {}
        posts = reversed(db.session.query(boardfinty).all())
        data.update({"message": 'success'})
        tmp = []
        for post in posts:
            tmp_dict = {}
            tmp_dict.update({f"id": post.id})
            tmp_dict.update({f"text": post.post_txt})
            tmp.append(tmp_dict)
        data.update({"posts": tmp})
        return data

    def put(self):
        db_form = boardfinty(post_txt=request.form['post_txt'])
        db.session.add(db_form)
        db.session.commit()
        return {'message': 'OK'}


api.add_resource(posts_api, f'/api/{api_v}/get/posts')


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


@app.route('/front', methods=['GET', 'POST'])
def front():
    return render_template("front.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
