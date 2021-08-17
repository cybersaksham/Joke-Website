from flask import Flask
import json

with open("config.json") as f:
    data = json.load(f)

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=data["debug"])
