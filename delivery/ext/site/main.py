from flask import render_template, request
from flask import Blueprint

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    name = request.args.get("name");
    return render_template("index.html", name=name)