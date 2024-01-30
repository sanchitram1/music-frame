const express = require("express");
const { json } = require("body-parser")
const app = express();

app.use(json());

const preimage = "https://i.scdn.co/image/ab67616d0000b27350068ff4b9b746b7cf2388aa";
const postimage = "https://i.scdn.co/image/ab67616d0000b273d803163d042298404f8547b0";

// set up the "/" route
app.get("/", (req, res) => {
  console.log(preimage);
  console.log(req);
  console.log(res);
  const body = `
  <!DOCTYPE html>
  <html>
    <head>
        <meta charSet="utf-8"/>
        <meta name="viewport" content="width=device-width"/>
        <meta property="fc:frame" content="vNext" />
        <meta property="fc:frame:image" content="${preimage}" />
        <meta property="fc:frame:button:1" content="Listen to my song" />
        <meta property="fc:frame:post_url" content="https://frame-f717fa7ddeeb.herokuapp.com/listen" />
    </head>
  </html>
    `;

  res.status(200).setHeader("Content-Type", "text/html").send(body);
});

app.post("/listen", (req, res) => {
  console.log(postimage);
  console.log(req);
  console.log(res);
  const body = `
  <!DOCTYPE html>
  <html>
    <head>
        <meta charSet="utf-8"/>
        <meta name="viewport" content="width=device-width"/>
        <meta property="fc:frame" content="vNext" />
        <meta property="fc:frame:image" content="${postimage}" />
    </head>
  </html>
    `;

  res.status(200).setHeader("Content-Type", "text/html").send(body);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
