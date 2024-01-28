from flask import Flask, render_template, request

app = Flask(__name__)

preimage_url = "https://media1.popsugar-assets.com/files/thumbor/QfDaGah_aK2iEyEKyS2P8OKgL-U=/0x0:5368x2818/fit-in/5368x3300/top/filters:format_auto():quality(85):upscale()/2020/02/07/036/n/45101125/2556ac155e3df83fba4965.26228381_.jpg"
postimage_url = "https://previews.123rf.com/images/phototrippingamerica/phototrippingamerica1804/phototrippingamerica180400033/99563791-three-golden-retrievers-look-to-their-owner-for-instruction-and-possibly-treats.jpg"


@app.route("/")
def index():
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
          <meta charset="utf-8"/>
          <meta name="viewport" content="width=device-width"/>
          <meta property="og:title" content="Pup Frame" />
          <meta property='og:image' content={preimage_url} />
          <meta property="fc:frame" content="vNext" />
          <meta property="fc:frame:image" content="{preimage_url}" />
          <meta property="fc:frame:button:1" content="Grow the pups" />
          <meta property="fc:frame:post_url" content="/grow" />
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
          <meta property='og:image' content={postimage_url} />
          <meta property="fc:frame" content="vNext" />
          <meta property="fc:frame:image" content="{postimage_url}" />
      </head>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
