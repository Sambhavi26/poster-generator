from flask import Flask,render_template
from urllib import request
import ssl
import json

ssl._create_default_https_context=ssl._create_unverified_context
base_url = "https://api.unsplash.com/photos/random/?collections=220388&client_id="
api_key = "e293bc76b28a5fbd1b2f51723c35f9cec1f9d0f1745d02d02f07b1a6f6542a14"
 
quote_url = "https://favqs.com/api/qotd"

app = Flask(__name__)

def getImageUrl():
    # TODO uncomment
    connection = request.urlopen(base_url + api_key)
    data = (connection.read())
    wallpaper_data = json.loads(data)
    url = (wallpaper_data.get("urls","not found").get("regular"))
    # url = "https://images.unsplash.com/photo-1549241520-425e3dfc01cb?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjc4OTU2fQ"
    return url

def getQuote():
    quote_connection = request.urlopen(quote_url)
    quote_data = json.loads(quote_connection.read())
    quote = (quote_data.get("quote").get("body"))
    author = (quote_data.get("quote").get("author"))
    return [quote,author]

@app.route("/")
def home():
    url = getImageUrl()

    quote_data = getQuote()
    quote = quote_data[0]
    author = quote_data[1]
    # url = "https://images.unsplash.com/photo-1549241520-425e3dfc01cb?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjc4OTU2fQ"
    return render_template("index.html", url=url,quote=quote,author=author)

@app.route("/<name>")
def about(name):
    return "This is " + name

@app.route("/get-image")
def handle_image_request():
    return getImageUrl()

@app.route("/get-quote")
def handle_quote_request():
    return json.dumps(getQuote())

if __name__ == "__main__":
    app.run(debug=True)