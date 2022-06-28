from app import db


class boardfinty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_txt = db.Column(db.String(), index=True)
    unixtime = db.Column(db.String(), default="0", index=True)

    def __repr__(self):
        return f'<id - {self.id}.'
