from flask import flask
app = Flask(_name_)

@app.route('/')

def index():
    return 'hello, world'