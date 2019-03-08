""" code and app structure based on Edwin C. tweet gen """


from modules.dictogram import Dictogram

def generate_dictograms(words, nth=4):
    """Generates a fourth order markov """
    dictograms = {}
    for index in range(len(words) -nth):
        key = tuple(words[index+i] for i in range(nth))
        if key not in dictograms:
            dictograms[key] = Dictogram()
        dictograms[key].add_count(words[index+nth])
        # print(dictograms)
    return dictograms

def random_walk(dict_of_dictograms):
    """ Takes a walk to return random word"""
    from random import choice
    from modules.sample import get_random_word
    key = choice(list(dict_of_dictograms))
    dictogram = dict_of_dictograms[key]
    random_weighted_word = get_random_word(dictogram)

    words = list(key)
    words.append(random_weighted_word)
    # print(words)
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
