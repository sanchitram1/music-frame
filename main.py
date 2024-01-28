import urllib.parse as urlparse
from requests import post, get, exceptions
from datetime import datetime
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, session
import secrets

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "http://localhost:5000/callback"

AUTH_URL = "https://accounts.spotify.com/authorize"  # base url for auth
TOKEN_URL = "https://accounts.spotify.com/api/token"  # refresh token
API_BASE_URL = "https://api.spotify.com/v1/"

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


def get_auth_header(token):
    """Format token for use in Authorization header"""
    return {"Authorization": f"Bearer {token}"}


def extract_info(json_data) -> dict:
    """Extract info from json data"""
    data = {
        "song": json_data["name"],
        "artist": json_data["artists"][0]["name"],
        "album": json_data["album"]["name"],
        "image": json_data["album"]["images"][0]["url"],
        "preview": json_data["preview_url"],
    }
    return data


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    scopes = "user-read-private user-read-email user-top-read"
    payload = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": scopes,
        "show_dialog": True,
    }
    auth_url = f"{AUTH_URL}?{urlparse.urlencode(payload)}"

    return redirect(auth_url)


@app.route("/http-error")
def error():
    return "HTTP Error, see logs"


@app.route("/callback")
def callback():
    if "error" in request.args:
        return jsonify({"error": request.args["error"]})

    if "code" in request.args:
        code = request.args["code"]
        payload = {
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = post(TOKEN_URL, data=payload, headers=headers)
        token_info = response.json()

        session["access_token"] = token_info["access_token"]
        session["refresh_token"] = token_info["refresh_token"]
        session["expires_in"] = datetime.now().timestamp() + token_info["expires_in"]

        return redirect("/top")


@app.route("/top")
def get_top_tracks():
    if "access_token" not in session:
        return redirect("/login")

    if datetime.now().timestamp() > session["expires_in"]:
        return redirect("/refresh_token")

    access_token = session["access_token"]
    headers = get_auth_header(access_token)
    params = {"limit": 5}
    response = get(f"{API_BASE_URL}me/top/tracks", headers=headers, params=params)
    try:
        response.raise_for_status()
        session["top_tracks"] = response.json()["items"]
        print(session["top_tracks"])
        # return redirect(url_for("song_info", **data))
        return redirect("/song")
    except exceptions.HTTPError as e:
        print(e)
        return redirect("/http-error")


@app.route("/song")
def song():
    if "top_tracks" not in session:
        return redirect("/login")
    return render_template("form.html")


@app.route("/song-info")
def song_info():
    if "top_tracks" not in session:
        return redirect("/login")
    song_index = int(request.args["song"]) - 1
    song_data = extract_info(session["top_tracks"][song_index])
    print(song_data)
    return render_template("song.html", **song_data)


@app.route("/refresh_token")
def refresh_token():
    if "refresh_token" not in session:
        return redirect("/login")

    if datetime.now().timestamp() > session["expires_in"]:
        refresh_token = session["refresh_token"]
        payload = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = post(TOKEN_URL, data=payload, headers=headers)
        token_info = response.json()

        session["access_token"] = token_info["access_token"]
        session["expires_in"] = datetime.now().timestamp() + token_info["expires_in"]

    return redirect("/top")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
