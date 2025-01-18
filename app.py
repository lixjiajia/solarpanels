from flask import Flask, render_template, request, jsonify

# import requests

app = Flask(__name__)


# Home route
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/solar-visualizations")
def visualize():
    print("GET")
    return render_template("./solar-visualizations.html", uploadErrors=[])
