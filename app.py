import os

import psycopg
from psycopg.types.json import Jsonb
from flask import Flask, render_template, request


app = Flask(__name__)


def save_submission(form_data):
    database_url = os.environ["DATABASE_URL"]
    with psycopg.connect(database_url) as connection:
        connection.execute(
            "INSERT INTO form_submissions (form_data) VALUES (%s)",
            (Jsonb(form_data),),
        )


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.files:
            return render_template("form.html", error="File uploads are not supported."), 400
        save_submission(request.form.to_dict(flat=False))
        return render_template("form.html", submitted=True)
    return render_template("form.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
