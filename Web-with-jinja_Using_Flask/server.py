from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_num = random.randint(1, 10)
    now = datetime.datetime.now()
    year = now.year
    return render_template("index.html", num=random_num, year=year)


@app.route("/guess/<name>")
def age_guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", names=name, gender=gender, age=age)


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/1473b379faec5e195afd"
    blog_respone = requests.get(blog_url)
    blog_data = blog_respone.json()
    return render_template("blog.html", blog=blog_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
