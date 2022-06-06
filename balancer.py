import requests
from flask import Flask, redirect

app = Flask(__name__)
robin = 0
redirect_urls = ["http://0.0.0.0:5001", "http://0.0.0.0:5002"]

@app.route("/")
def index():
    global robin
    robin += 1
    response = requests.get(redirect_urls[robin % 2])
    return response.content, response.status_code


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


