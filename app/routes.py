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
        for post in posts:
            tmp = []
            tmp.append(post.id)
            tmp.append(post.post_txt)
            if not ('posts' in data.keys()):
                data.update({'posts': tmp})
            else:
                data["posts"].append(tmp)
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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
