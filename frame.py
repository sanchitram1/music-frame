from flask import Flask

app = Flask(__name__)

image = "https://i.scdn.co/image/ab67616d0000b27350068ff4b9b746b7cf2388aa"
song = "Idol Eyes"
artist = "Common Saints"


@app.route("/")
def index():
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
          <meta property="fc:frame:button:1" content="Listen" />
          <meta property="fc:frame:post_url" content="https://frame-test-b1fbe9a5b014.herokuapp.com/listen" />
      </head>
    </html>
    """


@app.route("/listen", methods=["POST"])
def listen():
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
          <meta property="og:title" content="{song}" />
          <meta property='og:image' content={image} />
          <meta property="fc:frame" content="vNext" />
          <meta property="fc:frame:image" content="{image}" />
      </head>
      <body>
        <div>
            <p>Song: {song}</p>
            <p>Artist: {artist}</p>
        </div>
      </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
