# Import Modules
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

# Creating App
app = Flask(__name__)


# Main Route
@app.route('/')
def home():
    return render_template("index.html", lang=lang__, cat=cat__)


# Getting Joke
@app.route('/get_joke', methods=["POST"])
def get_joke():
    if request.method == "POST":
        try:
            # Language
            try:
                # Getting language from form
                lang_form__ = lang__[request.form["langSelect"]]
            except KeyError:
                # If language is not present in data
                return jsonify(error="Language is incorrect")
            # Category
            try:
                # Getting category from form
                cat_form__ = cat__[request.form["catSelect"]]
            except KeyError:
                # If category is not present in data
                return jsonify(error="Category is incorrect")
            # Generating Joke
            joke__ = pyjokes.get_joke(language=lang_form__,
                                      category=cat_form__)
            return jsonify(joke=str(joke__), error=None)
        except LanguageNotFoundError:
            # If language is not found
            return jsonify(error="Language not found.")
        except CategoryNotFoundError:
            # If category is not found
            return jsonify(error="Category not found.")
        except:
            # If other error occurs
            return jsonify(error="Some error occurred")


if __name__ == '__main__':
    app.run(debug=data["debug"])
