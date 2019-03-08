import random

def get_random_word(gram):
    histogram_type = str(type(gram).__name__ )

    if(histogram_type == "Listogram"):
        histogram = gram
    elif(histogram_type == "Dictogram"):
        histogram = [(key, value) for key, value in gram.items()]
    else:
        return

    total_words = gram.tokens

    words, counts = zip(*histogram)

    weights = [count/total_words for count in counts]

    random_word = ''
    while random_word == '':
        random_index = random.randrange(len(words))
        if random.random() < weights[random_index]:
            random_word = words[random_index]

    return random_word


if __name__ == '__main__':
    import sys
    from tokenize import get_words
    from cleanup import clean
    from dictogram import Dictogram
    words = get_words(sys.argv[1])
    cleaned_words = clean(words)
    listogram = Dictogram(cleaned_words)
    random_weighted_word = get_random_word(listogram)

    # print random weighted word
    print(random_weighted_word)
        


