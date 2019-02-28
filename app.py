from flask import Flask, render_template
# need to add bootstrap module
# from flask_bootstrap import Bootstrap
app = Flask(__name__)
# from flask import render_template
# from app import app
from modules import linkedlist

@app.route('/')
def main():
    app.config["TRAP_BAD_REQUEST_ERRORS"] = True
    app.run(debug=True)
    print("Hello?????")
    return render_template('index.html')

# so that you do not have restart the app to debug
if __name__ == "__main__":
    app.config["TRAP_BAD_REQUEST_ERRORS"] = True
    app.run(debug=True)
    print("Hello?????")
