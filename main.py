from flask import Flask, render_template, request, jsonify
import pyjokes
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


@app.route('/get_joke', methods=["POST"])
def get_joke():
    if request.method == "POST":
        try:
            lang_form__ = request.form["langSelect"]
            cat_form__ = request.form["catSelect"]
            joke__ = pyjokes.get_joke(language=lang__[lang_form__],
                                      category=cat__[cat_form__])
            return jsonify(joke=str(joke__), error=None)
        except Exception as e:
            return jsonify(error=str(e))


if __name__ == '__main__':
    app.run(debug=data["debug"])
