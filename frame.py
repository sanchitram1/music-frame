from flask import Flask, render_template
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route("/")
def index():
    return render_template("frame.html")
