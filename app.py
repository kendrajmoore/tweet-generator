from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
# from flask import render_template
# from app import app

@app.route('/')
def main():
    return render_template('index.html')

