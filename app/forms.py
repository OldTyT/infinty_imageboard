from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


class add_post(FlaskForm):
    post_txt = StringField('Текст поста', validators=[DataRequired()])
    submit = SubmitField('Отправить')
