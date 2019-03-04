import sys
import re
import random
import tokenize
import cleanup
#three

def dictogram_words(words):
    dictogram = {}
    for word in words:
        if word not in (dictogram):
            dictogram[word] = 0
        dictogram[word] += 1
    return dictogram

def sum(histogram):
    print(histogram)
    total = len(histogram)
    # total = (sum(histogram.values()))
    return total


if __name__ == "__main__":
    params = sys.argv[1:]
    file = params[0]
    word_list = cleanup.cleanup(file)
    dicts = dictogram_words(word_list)
    # print(dicts)
    total = sum(dicts)
    print(total)