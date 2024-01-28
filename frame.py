from flask import Flask

app = Flask(__name__)

with open("data.json", "r") as f:
    data = f.read()


@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
      <head>
          <meta charset="utf-8"/>
          <meta name="viewport" content="width=device-width"/>
          <meta property="og:title" content="Listen In" />
          <meta property="fc:frame" content="vNext" />
          <meta property="fc:frame:image" content="👂🏾" />
          <meta property="fc:frame:button:1" content="Listen" />
          <meta property="fc:frame:post_url" content="/listen" />
      </head>
    </html>
    """


@app.route("/grow", methods=["POST"])
def grow():
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
          <meta property="og:title" content="Pup Frame" />
          <meta property='og:image' content={data['song']} />
          <meta property="fc:frame" content="vNext" />
          <meta property="fc:frame:image" content="{data['image']}" />
      </head>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
