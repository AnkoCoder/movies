from flask import Flask, render_template
import json

app = Flask(__name__)

schedule = {
    "Bekmambetov Cinema" : {
        "id": "1",
        "movies": [
            {
                "name": "Девятое", 
                "time": "11:40"
            }
        ]
    }
}


@app.route('/')
def hello():
    with open('theatres.json') as f:
        theatres = json.load(f)
        result = {}
    for id, name in theatres.items():
        result[name] = id
    with open('db.json') as f:
        movies = json.load(f)
    schedule = {}
    for movie in movies:
        theatre = movie['theatre']
        if theatre not in schedule:
            schedule[theatre] = {
                "movies": [],
                "id": result[theatre]
            }
        schedule[theatre]["movies"].append(
            {
                'name': movie['name'],
                'time': movie['time']
            }
        )

    return render_template("index.html", schedule=schedule)


@app.route('/cinema/<cinema_id>')
def cinema(cinema_id):
    with open('db.json') as f:
        movies = json.load(f)
    with open('theatres.json') as f:
        theatres = json.load(f)
        theatre = theatres[cinema_id]
        movies = [movie for movie in movies if movie["theatre"] == theatre]
    return render_template("cinema.html", theatre=theatre, movies=movies)
