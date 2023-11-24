import wtforms
from flask import jsonify
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, ValidationError
from wtforms.validators import length, DataRequired, EqualTo, email, Length
from models import EmailCaptchaModel,User
from werkzeug.security import check_password_hash


class LoginFrom(wtforms.Form):
    user_email = wtforms.StringField(validators=[email()])
    user_password = wtforms.StringField(validators=[length(min=3, max=20)])

    def validate_user_email(self, field):
        email = field.data
        user_model = User.query.filter_by(user_email=email).first()
        if not user_model:
            raise ValidationError("email")

    def validate_user_password(self, field):
        user_password = field.data
        user_email = self.user_email.data
        user_model = User.query.filter_by(user_email=user_email).first()
        if user_model and not check_password_hash(user_model.user_password,user_password):
            raise wtforms.ValidationError("password")


class RegisterForm(wtforms.Form):
    user_email = wtforms.StringField(validators=[DataRequired("email cannot be none"), email()])
    user_first_name = wtforms.StringField(validators=[DataRequired("username cannot be none"), length(min=1, max=30)])
    user_last_name = wtforms.StringField(validators=[DataRequired("username cannot be none"), length(min=1, max=30)])
    user_password = wtforms.StringField(validators=[DataRequired("password cannot be none"), length(min=6, max=40)])
    captcha = wtforms.StringField(validators=[length(min=6, max=6)])


    def validate_user_email(self, field):
        email = field.data
        user_model = User.query.filter_by(user_email=email).first()
        if user_model:
            raise ValidationError("mail")


    def validate_captcha(self, field):
        captcha = field.data
        email = self.user_email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if not captcha_model or captcha_model.captcha != captcha:
            raise ValidationError("captcha")


class ForgetFormEmail(wtforms.Form):
    user_email = wtforms.StringField(validators=[email()])
    captcha = wtforms.StringField(validators=[length(min=6, max=6)])

    def validate_user_email(self, field):
        email = field.data
        user_model = User.query.filter_by(user_email=email).first()
        if not user_model:
            raise wtforms.ValidationError("not register yet")

    def validate_captcha(self, field):
        captcha = field.data
        email = self.user_email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if not captcha_model or captcha_model.captcha != captcha:
            raise wtforms.ValidationError("wrong validation code")


class ForgetFormPassword(wtforms.Form):
    user_password = wtforms.StringField(validators=[DataRequired("password cannot be none"), length(min=3, max=20)])
    confirm = wtforms.StringField(validators=[EqualTo('user_password')])