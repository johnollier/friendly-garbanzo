from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.files:
            return render_template("form.html", error="File uploads are not supported."), 400
        return render_template("form.html", submitted=True)
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
