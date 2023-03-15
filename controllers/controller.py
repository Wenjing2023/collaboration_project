from flask import render_template

from app import app
from models.order_list import orders


@app.route("/orders")
def index():
    return render_template("index.html", title="T&W HOME", order_list=orders)


@app.route("/orders/<index>")
def read(index):
    # find the order using the index
    order = orders[int(index) - 1]
    return render_template("order.html", order=order)
