from flask import Blueprint
from flask import render_template

bp = Blueprint("site", __name__)

site_name = "DevFoods"
site_subtitle = "O melhor site de delivery do Brasil"
items = list(range(4))

@bp.route("/")
def index():
    return render_template("index.html", site_name=site_name, site_subtitle=site_subtitle, items=items)

@bp.route("/sobre")
def about():
    return render_template("about.html", site_name=site_name, site_subtitle=site_subtitle)

@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html", site_name=site_name, site_subtitle=site_subtitle, items=items)