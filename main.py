from flask import Flask, render_template
import json

# Global Variables
with open("config.json") as f:
    data = json.load(f)
with open("static/data.json") as f:
    langData = json.load(f)
    lang__, cat__ = langData["languages"], langData["categories"]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", lang=lang__, cat=cat__)


if __name__ == '__main__':
    app.run(debug=data["debug"])
