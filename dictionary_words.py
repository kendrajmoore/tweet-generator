
import random
import sys


def file():
    f = open("/usr/share/dict/words", "r")
    words = f.read().split()
    f.close()
    return words


def dictionary(number):
    words_spaced = ""
    wordsList = []
    x = 0

    while x < number:
        wordsList.append(words[random.randint(0, (len(words) - 1))])
        x += 1

    for word in wordsList:
        words_spaced += str(word)
        words_spaced += " "

    return words_spaced

if __name__ == '__main__':
    number = sys.argv[1]
    number = int(number)
    words = file()
    print(dictionary(number))