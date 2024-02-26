from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Definitely not in Staging, but good old prod!"
