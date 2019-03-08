from modules.dictogram import Dictogram


def generate_dictograms(words):
    dictograms = {}
    for index in range(len(words) -1):
        if words[index] not in dictograms:
            dictograms[words[index]] = Dictogram()
        dictograms[words[index]].add_counts(words[index+1])
        # print(dictograms)
    return dictograms

def random_walk(dict_of_dictograms):
    from random import choice
    from modules.sample import get_random_word
    key = choice(list(dict_of_dictograms))
    # print(key)
    dictogram = dict_of_dictograms[key]
    # print(dictogram)
    random_weighted_word = get_random_word(dictogram)
    return [key, random_weighted_word]

if __name__ == '__main__':
    import sys
    from tokenize import get_words
    from cleanup import clean
    words = get_words(sys.argv[1])
    cleaned_words = clean(words)
    dictograms = generate_dictograms(cleaned_words)
    # print(dictograms)
    random_words = []
    for i in range(int(sys.argv[2])//2):
        walk = random_walk(dictograms)
        random_words.append(walk[0])
        random_words.append(walk[1])

    # print some test results
    print(random_words)
