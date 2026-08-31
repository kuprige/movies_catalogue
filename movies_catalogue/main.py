from flask import Flask, render_template, abort

app = Flask(__name__)

MOVIES = [
    {"id": 1, "title": "Film 1", "overview": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente esse necessitatibus neque.", "poster": "https://via.placeholder.com/500x325?text=500x325"},
    {"id": 2, "title": "Film 2", "overview": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente esse necessitatibus neque.", "poster": "https://via.placeholder.com/500x325?text=500x325"},
    {"id": 3, "title": "Film 3", "overview": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente esse necessitatibus neque.", "poster": "https://via.placeholder.com/500x325?text=500x325"},
    {"id": 4, "title": "Film 4", "overview": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente esse necessitatibus neque.", "poster": "https://via.placeholder.com/500x325?text=500x325"},
]

@app.route('/')
def homepage():
    return render_template("homepage.html", movies=MOVIES)

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = next((m for m in MOVIES if m["id"] == movie_id), None)
    if not movie:
        abort(404)
    return render_template("movie_detail.html", movie=movie)

if __name__ == "__main__":
    app.run(debug=True)
