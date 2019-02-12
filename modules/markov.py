# I need a dictogram to start
from dictogram import Dictogram

def make_dictograms(words):
    "Takes in a list of words and makes a dictogram for that word"
    dictograms = {}
    # cycle through all the words except the last one because we do not care what follows
    for index in range(len(words) -1):
        if words[index] not in dictograms:
            dictograms[words[index]] = Dictogram()
        dictograms[words[index]].add_count(words[index+1])
    return dictograms


if __name__ == "__main__":
    # better to place at the bottm of the file
    import sys

