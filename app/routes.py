from flask import render_template, redirect, url_for, request, send_from_directory
from app.models import *
from app import app, db, api
from app.forms import *
from flask_json import as_json
from flask_restful import Resource, Api
from datetime import datetime

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
            tmp_dict.update({f"unixtime": post.unixtime})
            tmp.append(tmp_dict)
        data.update({"posts": tmp})
        return data

    def put(self):
        db_form = boardfinty(post_txt=request.data.decode("utf-8"), unixtime=datetime.now().timestamp())
        db.session.add(db_form)
        db.session.commit()
        return {'message': 'OK'}


api.add_resource(posts_api, f'/api/{api_v}/get/posts')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
