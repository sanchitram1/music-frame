from flask import Flask, request, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

album = "https://i.scdn.co/image/ab67616d0000b27350068ff4b9b746b7cf2388aa"
song = "Idol Eyes"
artist = "Common Saints"
preview = "https://p.scdn.co/mp3-preview/f5c6f9354fa9902d2ea5406c64b2a53ec70755e3?cid=467193f35468464cbda5989d0ebe23e7"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["button_clicked"] = True
        return render_page(True)
    else:
        return render_page(session.get("button_clicked", False))


def render_page(button_clicked):
    print(button_clicked)

    # always display it as an image of the song you're listening to
    image = album
    print(image)

    # display the song and artist, only if the button has been clicked
    tag_html = f'<meta property="og:description" content="{song} by {artist}" />'

    # display the button only if it hasn't been clicked
    button_html = (
        """
        <form method="post" action="/">
            <button type="submit" name="button" value="Listen">Listen</button>
        </form>
    """
        if not button_clicked
        else ""
    )
    print(button_html)
    fc_frame_button = (
        '<meta property="fc:frame:button:1" content="Listen" />'
        if not button_clicked
        else ""
    )
    print(fc_frame_button)

    return f"""
    <!DOCTYPE html>
    <html>
      <head>
          <meta charset="utf-8"/>
          <meta name="viewport" content="width=device-width"/>
          <meta property="og:title" content="Listen" />
          <meta property="og:image" content="{image}" />
          {tag_html}
          <meta property="fc:frame" content="vNext" />
          <meta property="fc:frame:image" content="{image}" />
          {fc_frame_button}
      </head>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
