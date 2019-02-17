# I need a dictogram to start
from dictogram import Dictogram
from random import choice
from sample import one_word
from histogram import histogram


def make_dictograms(words):
    "Takes in a list of words and makes a dictogram for that word"
    dictograms = {}
    # cycle through all the words except the last one because we do not care what follows
    for index in range(len(words) -1):
        if words[index] not in dictograms:
            dictograms[words[index]] = Dictogram()
        dictograms[words[index]].add_count(words[index+1])
    return dictograms

def random_walk(dictogram_of_dictograms):
    "Takes a dictogram and determine the weight"
    key = choice(list(dictogram_of_dictograms))
    dictogram = dictogram_of_dictograms[key]
    random_weighted_word = one_word(histogram)

    return [key, random_weighted_word]



if __name__ == "__main__":
    # better to place at the bottm of the file
    import sys
    from tokenize import words_list
    from cleanup import cleanup
    words = words_list(sys.argv[1])
    clean_corups = cleanup(words)
    dictograms = make_dictograms(clean_corups)
    print(dictograms)
    random_words = []
    for i in range(int(sys.argv[2])//2):
        walk = random_walk(dictograms)
        random_words.append(walk[0])
        random_words.append(walk[1])

    # print some test results
    print(random_words)

