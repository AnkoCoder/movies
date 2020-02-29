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