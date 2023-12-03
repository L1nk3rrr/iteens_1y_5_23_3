from flask import Flask, render_template

app = Flask('oderman', template_folder="templates", static_folder="static")

@app.route('/')
@app.route('/index')
def index_view():
    return render_template("index.html")

@app.route('/hello-world')
def hello_world_view():
    return 'Hello from neeeeeeew view world'


@app.route('/day')
def day_view():
    return 'Have a nice day'

@app.route('/path1')
def path1():
   return 'Це path1'

@app.route('/path2/')
def path2():
   return 'Це path2'

# Якщо є слеш в кінці роута, то буде працювати запит і з роутом і без.
# Якщо слеш не вказувати, то буде працювати тільки без слешу


if __name__ == "__main__":
    # host = 'localhost'
    # port = 5001
    app.run(debug=True)