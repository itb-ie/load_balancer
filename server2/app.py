from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "You have been assigned to server2"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
