from crypt import methods
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>\n"

@app.route("/set_name", methods=['PUT'] )
def change_password():
    return f"<p>your name is {request.form['name']}!</p>\n"

@app.route("/login", methods=['POST'])
def login():
    return f"<p>your login is {request.form['username']}</p>\n"

app.run(host='0.0.0.0', port=5000)