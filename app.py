from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def hello():
    with open('db.json') as f:
        movies = json.load(f)
    theatres = {}
    for movie in movies:
        theatre = movie['theatre']
        if theatre not in theatres:
            theatres[theatre] = []
        theatres[theatre].append(
            {
                'name': movie['name'],
                'time': movie['time']
            }
        )
    return render_template("index.html", theatres=theatres)


@app.route('/cinema/<cinema_id>')
def show_post(cinema_id):
    with open('db.json') as f:
        movies = json.load(f)
    with open('theatres.json') as f:
        theatres = json.load(f)
        theatre = theatres[cinema_id]
        movies = [movie for movie in movies if movie["theatre"] == theatre]
    return render_template("cinema.html", theatre=theatre, movies=movies)
