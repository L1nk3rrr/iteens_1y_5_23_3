from flask import Flask, render_template

app = Flask(__name__)

data = [
    {"name": "George", "score": 90},
    {"name": "Valentyn", "score": 30},
    {"name": "Mikha", "score": 70},
    {"name": "Leonti", "score": 96},
]



@app.route('/')
@app.route('/home')
def index():
    return render_template("base.html", title="Jinja and Flask")


@app.route('/results/')
def get_results():
    context = {
        "title": "Results",
        "test_name": "Python Challenge",
        "max_score": 100,
        "students": data,
    }
    return render_template("results.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
