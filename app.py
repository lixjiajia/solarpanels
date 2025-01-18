from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')
