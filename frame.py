from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

# Predefined variables
preimage = "https://i.scdn.co/image/ab67616d0000b27350068ff4b9b746b7cf2388aa"
postimage = "https://i.scdn.co/image/ab67616d0000b273d803163d042298404f8547b0"
song = "Idol Eyes"
artist = "Common Saints"


@app.route("/", methods=["GET", "POST"])
def index():
    print(request.method)
    if request.method == "POST":
        return handle_post_request()
    else:
        return render_page(False)


def handle_post_request():
    # Parse the JSON data from the POST request
    data = request.json
    print(data)
    button_id = data.get("untrustedData", {}).get("button_id")

    # Check which button was clicked and update the state accordingly
    if button_id == 1:
        print("Button was clicked")
        return render_page(True)
    else:
        return render_page(False)


def render_page(button_clicked):
    # Always display it as an image of the song you're listening to
    image = preimage if not button_clicked else postimage

    # Display the song and artist, only if the button HAS been clicked
    tag_html = (
        f'<meta property="og:description" content="{song} by {artist}" />'
        if button_clicked
        else ""
    )

    # Display the button only if it HASN'T been clicked
    fc_frame_button = (
        '<meta property="fc:frame:button:1" content="Listen" />'
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
          {tag_html}
          <meta property="fc:frame" content="vNext" />
          <meta property="fc:frame:image" content="{image}" />
          {fc_frame_button}
      </head>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
