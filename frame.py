from flask import Flask, request, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

preimage = "https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_CMYK_Black.png"
album = "https://i.scdn.co/image/ab67616d0000b27350068ff4b9b746b7cf2388aa"
song = "Idol Eyes"
artist = "Common Saints"
preview = "https://p.scdn.co/mp3-preview/f5c6f9354fa9902d2ea5406c64b2a53ec70755e3?cid=467193f35468464cbda5989d0ebe23e7"

# <meta property="fc:frame:post_url" content="https://frame-test-5dd2ced0e874.herokuapp.com/listen" />


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["button_clicked"] = True
        return render_page(True)
    else:
        return render_page(session.get("button_clicked", False))


def render_page(button_clicked):
    print(button_clicked)
    image = preimage if not button_clicked else album
    print(image)
    button_html = (
        """
        <form method="post" action="/">
            <button type="submit" name="button" value="Listen">Listen</button>
        </form>
    """
        if not button_clicked
        else ""
    )
    fc_frame_button = (
        '<meta> property="fc:frame:button:1" content="Listen" />'
        if not button_clicked
        else ""
    )

    return f"""
    <!DOCTYPE html>
    <html>
      <head>
          <meta charset="utf-8"/>
          <meta name="viewport" content="width=device-width"/>
          <meta property="og:title" content="Listen" />
          <meta property="og:image" content="{image}" />
          <meta property="fc:frame" content="vNext" />
          <meta property="fc:frame:image" content="{image}" />
          {fc_frame_button}
          <title> Listen </title>
      </head>
      <body>
        {button_html}
      </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
