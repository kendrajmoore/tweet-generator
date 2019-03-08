from flask import Flask 
from dictionary_words import sentence
app = Flask(__name__)

@app.route('/')
def index():
    ''' sentence generator '''
    string = sentence()
    return string

@app.route('/hello')
def hello_world():
    ''' Hello World test '''
    return 'Hello World'


if __name__ == '__main__':
    index()