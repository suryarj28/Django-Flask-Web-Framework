from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__)

blog_url = "https://api.npoint.io/117c09fda2f9aeeedc5a"
blog_response = requests.get(blog_url).json()


@app.route('/')
def index():
    return render_template("index.html", all_post=blog_response)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:indexes>")
def show_post(indexes):
    requested_post = None
    for blog_post in blog_response:
        if blog_post["id"] == indexes:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#     print(name)
#     print(email)
#     print(phone)
#     print(message)
#     return '<img src="https://cdn.pixabay.com/photo/2014/04/03/10/51/mail-311519_960_720.png">'

@app.route("/contact", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)


