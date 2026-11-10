from flask import Flask, redirect, render_template, request, url_for
import requests

app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:5001/api/add-user"


@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit():
    user_data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
    }

    # Send data to backend service
    requests.post(BACKEND_URL, json=user_data)

    return redirect(url_for("success"))


@app.route("/success", methods=["GET"])
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)