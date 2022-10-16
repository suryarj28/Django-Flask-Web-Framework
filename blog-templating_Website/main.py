from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/1473b379faec5e195afd"
blog_body = requests.get(blog_url).json()
post_objects = []
for post in blog_body:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog=post_objects)


@app.route("/post/<int:index>")
def get_blog(index):
    request_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            request_post = blog_post
    return render_template("post.html", post=request_post)


if __name__ == "__main__":
    app.run(debug=True)
