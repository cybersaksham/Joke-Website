from flask import Flask, render_template, request, jsonify
import pyjokes
from pyjokes.pyjokes import LanguageNotFoundError, CategoryNotFoundError
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
            try:
                lang_form__ = lang__[request.form["langSelect"]]
            except KeyError:
                return jsonify(error="Language is incorrect")
            try:
                cat_form__ = cat__[request.form["catSelect"]]
            except KeyError:
                return jsonify(error="Category is incorrect")
            joke__ = pyjokes.get_joke(language=lang_form__,
                                      category=cat_form__)
            return jsonify(joke=str(joke__), error=None)
        except LanguageNotFoundError:
            return jsonify(error="Language not found.")
        except CategoryNotFoundError:
            return jsonify(error="Category not found.")
        except Exception as e:
            return jsonify(error=str(e))


if __name__ == '__main__':
    app.run(debug=data["debug"])
