from flask import Flask, render_template
# need to add bootstrap module
# from flask_bootstrap import Bootstrap
app = Flask(__name__)
# from flask import render_template
# from app import app
import markov

app.longer_model = markov.markov_chain(markov.open_file('twilight.txt'))

@app.route('/')
def main():
    return markov.generate_sentence(app.longer_model)
    app.config["TRAP_BAD_REQUEST_ERRORS"] = True
    app.run(debug=True)
    print("Hello?????")
    return render_template('index.html')

# so that you do not have restart the app to debug
if __name__ == "__main__":
    app.config["TRAP_BAD_REQUEST_ERRORS"] = True
    app.run(debug=True)
    print("Hello?????")
