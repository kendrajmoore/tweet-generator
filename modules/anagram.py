import sys
import random

def get_words():
    #get words 
    f = open("/usr/share/dict/words", "r")
    words = f.read().split()
    f.close()
    return words


if __name__ in '__main__':
    words_list = get_words()
    