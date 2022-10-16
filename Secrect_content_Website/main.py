from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[Email("invalid email address.")])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8, max=16, message="field must have at least 8 characters long.")])
    submit = SubmitField(label="submit")


app = Flask(__name__)
app.secret_key = "ms-dhoni-no7"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            # print(f"email: {login_form.email.data}")
            # print(f"password: {login_form.password.data}")
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
