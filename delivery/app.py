from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    if (name):
        return f"<h1>Hello, {name}!</h1>"
    return "<h1>Hello, world!</h1>"

@app.route("/sobre")
def sobre():
    return "<p>Sobre o site...</p>"