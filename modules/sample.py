import random

def get_random_word(gram):
    """ Determines the type of histogram so that it can retrieve word tokens """
    histogram_type = str(type(gram).__name__ )

    if(histogram_type == "Listogram"):
        histogram = gram
    elif(histogram_type == "Dictogram"):
        histogram = [(key, value) for key, value in gram.items()]
    else:
        return
    # count all the words to get my tokens
    total_words = gram.tokens

    words, counts = zip(*histogram)

    weights = [count/total_words for count in counts]

    random_word = ''
    while random_word == '':
        random_index = random.randrange(len(words))
        # print(random_index)
        if random.random() < weights[random_index]:
            random_word = words[random_index]
            # print(random_word)

    return random_word


if __name__ == '__main__':
    import sys
    from tokenize import get_words
    from cleanup import clean
    from dictogram import Dictogram
    words = get_words(sys.argv[1])
    cleaned_words = clean(words)
    # print(cleaned_words)
    listogram = Dictogram(cleaned_words)
    random_weighted_word = get_random_word(listogram)

    # print random weighted word
    print(random_weighted_word)
        


