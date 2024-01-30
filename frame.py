from flask import Flask, request
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

# Predefined variables
preimage = "https://i.scdn.co/image/ab67616d0000b27350068ff4b9b746b7cf2388aa"
postimage = "https://i.scdn.co/image/ab67616d0000b273d803163d042298404f8547b0"


@app.route("/", methods=["GET"])
def index():
    print(request.method)
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
          <meta charset="utf-8"/>
          <meta name="viewport" content="width=device-width"/>
          <meta property="fc:frame" content="vNext" />
          <meta property="fc:frame:image" content="{preimage}" />
          <meta property="fc:frame:button:1" content="Listen" />
          <meta property="fc:frame:post_url" content="https://frame-test-5dd2ced0e874.herokuapp.com/listen" />
      </head>
    </html>
    """


@app.route("/listen", methods=["POST"])
def listen():
    """can only post here"""
    print("Listen post?")
    print(request.method)
    print(request.json)
    return final()


def final():
    """No buttons or post url"""
    print("Final method called")
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
          <meta charset="utf-8"/>
          <meta name="viewport" content="width=device-width"/>
          <meta property="fc:frame" content="vNext" />
          <meta property="fc:frame:image" content="{postimage}" />
      </head>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
