from flask import Flask
import random

random_number = random.randint(0, 9)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1>Guess a number between 0 and 9 For ex: server address/guess no. </h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return '<h1 "color: purple">Too High! </h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    elif guess < random_number:
        return '<h1>Too Low! </h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1>Correct!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
