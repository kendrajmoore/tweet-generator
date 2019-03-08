from modules.dictogram import Dictogram


def generate_dictograms(words, nth=4):
    '''Takes a list of words and generates a dictionary of dictograms of each word directly following each tuple of words nth length'''

    # create a dictionary to hold our dictograms
    dictograms = {}

    # First we must iterate through the words list, exluding the last item
    for index in range(len(words) - nth):

        # build tuple for key
        key = tuple(words[index+i] for i in range(nth))

        # check if the word is not in dictionary of word histograms already
        if key not in dictograms:
            # create new dictogram for the word in dictionary of dictograms
            dictograms[key] = Dictogram()
        # add count of word following word to dictogram
        dictograms[key].add_count(words[index+nth])

    # return dictograms dictionary
    return dictograms


def random_walk(dict_of_dictograms):
    '''Takes a dictionary of dictograms and returns a random weighted traversal along the markov chain'''
    from random import choice

    # we will use our random weighted sample word generator file to help us
    from modules.sample import get_random_word

    # first pick a random dictogram
    key = choice(list(dict_of_dictograms))
    dictogram = dict_of_dictograms[key]

    # now pick a random weighted word
    random_weighted_word = get_random_word(dictogram)

    # words
    words = list(key)
    words.append(random_weighted_word)

    # return the words
    return words


if __name__ == '__main__':
    import sys
    from tokenize import get_words
    from cleanup import clean
    words = get_words(sys.argv[1])
    cleaned_words = clean(words)
    dictograms = generate_dictograms(cleaned_words)
    random_words = []
    for i in range(int(sys.argv[2])//3):
        walk = random_walk(dictograms)
        random_words.append(walk[0])
        random_words.append(walk[1])

    # print some test results