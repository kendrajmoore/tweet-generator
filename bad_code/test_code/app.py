from app import app
from histogram import histogram
from stochastic_sample import weighted_random_select
import re, string
from flask import Flask, jsonify, render_template

@app.route('/')
@app.route('/index')
def index():
    word_file = 'text2.txt'
    text =  open(word_file).read()
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower()
    words_from_text = (text.translate(translator)).split()
    # sorts words alphabetically
    words_from_text = sorted(words_from_text)
    hist = histogram(words_from_text)
    sentence = []
    for i in range(10):
        select_word = weighted_random_select(hist, words_from_text)
        sentence.append(select_word)
    print(sentence)
    words = " ".join(sentence)

    return render_template("base.html", title='Home Page',words=words)