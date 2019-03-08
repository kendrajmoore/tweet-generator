""" code and app structure based on Edwin C. tweet gen """


from modules.tokenize import get_words
from modules.cleanup import clean
from modules.dictogram import Dictogram
from modules.sample import get_random_word
from modules.sentence import generate_sentence
from modules.markov2 import generate_dictograms, random_walk
from random import randint


def random_sentence(corpus, min_num_of_words=15, max_num_of_words=20):
    """Defines number of words for tweet generator sentence """
    num_of_word = randint(min_num_of_words, max_num_of_words)
    words = get_words(corpus)
    cleaned_words = clean(words)
    listogram = Dictogram(cleaned_words)
    random_weighted_words = [get_random_word(listogram) for random_weighted_word in range(num_of_words)]
    sentence = generate_sentence(random_weighted_words)
    return sentence

def random_markov_sentence(corpus, min_num_of_walks=3, max_num_of_walks=4):
    """ Tells the generator how manny walks of markov to make"""
    num_of_walks = randint(min_num_of_walks, max_num_of_walks)
    words = get_words(corpus)
    cleaned_words = clean(words)
    dictograms = generate_dictograms(cleaned_words)
    random_words = []
    for _ in range(num_of_walks):
        walk = random_walk(dictograms)
        random_words.extend(walk)
    sentence = generate_sentence(random_words)
    return sentence

if __name__ == "__main__":
    import sys
    sentence = random_sentence(sys.argv[1], sys.argv[2], sys.argv[3])
    print(sentence)