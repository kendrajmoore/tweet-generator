import re
import sys
import random
import sample
from dictogram import Dictogram

def cleanup(text):
    with open(text, 'r') as original_text:
        no_chapters = re.sub('[A-Z]{3,}', ' ', uncl.read())




def tokenize(remove_punctuation):
    """I need word tokens """
    source = remove_punctuation.split()
    return source

def start_token(dictionary):
    start



if __name__ == "__main__":
    params = sys.argv[1:]
    file = params[0]
    texts = cleanup(file)
    tokens = tokenize(texts)
    print(tokens)

