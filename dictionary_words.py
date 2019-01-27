import random
import sys


def file():
    """ get words from words file """
    f = open("/usr/shar/dict/words", "r")
    words = f.read().split()
    f.close()
    return words

def dict(number):
    wordsDict = []
    words_spaced = ""
    x = 0

    while x < number:
        wordsDict.append(words[random.randint(0, (len(words) - 1))])
        x += 1

    for word in wordsDict:
        words_spaced += str(word)
        words_spaced += " "

    return words_spaced

if __name__ == '__main__':
    number = sys.argv[1]
    number = int(number)
    words = file()
    print(dict(number))