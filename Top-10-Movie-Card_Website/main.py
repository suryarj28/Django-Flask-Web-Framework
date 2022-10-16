from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

# API Data

MOVIE_DB_API_KEY = "dc151975ce576e2c8935827447438060"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '----------------------'
Bootstrap(app)

# Creating Database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-movies-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# db.create_all()
# db.session.commit()


# Creating Table

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


# db.create_all()
# db.session.commit()

new_movies = Movies(id=1, title="Life Of Pi", year=2012,
                    description="Life of Pi is a 2012 adventure-drama film directed and produced by Ang Lee and written by David Magee.",
                    rating=4.8, ranking=1, review="A great masterpiece",
                    img_url="https://i.pinimg.com/550x/21/ac/47/21ac471a1f2a637dcdb3f4317c7a9bae.jpg")


# db.session.add(new_movies)
# db.session.commit()

# Rating Form data


class RatingForm(FlaskForm):
    rating = FloatField(validators=[DataRequired()], label="Your Rating out of 10.00 e.g. 7.5")
    review = StringField(validators=[DataRequired()], label="Your Review")
    Submit = SubmitField(label="Done")


# Rating Form data


class AddForm(FlaskForm):
    movie = StringField(validators=[DataRequired()], label="Movie Title")
    submit = SubmitField(label="Add Movie")


# Home page


@app.route("/")
def home():
    all_movies = Movies.query.order_by(Movies.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
        db.session.commit()
    all_new_movies = Movies.query.order_by(Movies.ranking).all()
    db.session.commit()

    return render_template("index.html", movies=all_new_movies)


# Add Movies with APIs


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        movie_name = form.movie.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_name})
        data = response.json()['results']
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


# Find Movies

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    print(movie_api_id)
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movies(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['backdrop_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("home", id=new_movie.id))


# Edit ratings

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RatingForm()
    movie_id = request.args.get("id")
    movie_selected = Movies.query.get(movie_id)
    if form.validate_on_submit():
        to_update = Movies.query.get(movie_id)
        to_update.rating = request.form["rating"]
        to_update.review = request.form["review"]
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie_selected, form=form)


# Delete movies

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movies.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
