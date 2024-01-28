from flask import Flask

app = Flask(__name__)

with open("data.json", "r") as f:
    data = f.read()


@app.route("/")
def index():
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
          <meta charset="utf-8"/>
          <meta name="viewport" content="width=device-width"/>
          <meta property="og:title" content="Listen" />
          <meta property="fc:frame" content="vNext" />
          <meta property="fc:frame:image" content="{data['image']}" />
          <meta property="fc:frame:button:1" content="Listen" />
          <meta property="fc:frame:post_url" content="/listen" />
      </head>
    </html>
    """


@app.route("/listen", methods=["POST", "GET"])
def listen():
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
          <meta property="og:title" content="{data['song']}" />
          <meta property='og:image' content={data['image']} />
          <meta property="fc:frame" content="vNext" />
          <meta property="fc:frame:image" content="{data['image']}" />
      </head>
      <body>
        <audio class="audio-player" controls autoplay loop>
            <source src="{data['preview']}" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        <div>
            <p>Song: {data['song']}</p>
            <p>Artist: {data['artist']}</p>
        </div>
      </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
