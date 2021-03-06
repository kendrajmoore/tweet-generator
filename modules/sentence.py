
def generate_sentence(words):
    """Generates a tweet and capitializes first letter """
    words[0] = words[0].capitalize()
    print(words[0])
    sentence = ' '.join(words)+'.'
    # print(sentence)
    return sentence

if __name__ == '__main__':
    import sys
    from tokenize import get_words
    from cleanup import clean
    from dictogram import Dictogram
    from sample import get_random_word
    words = get_words(sys.argv[1])
    cleaned_words = clean(words)
    listogram = Dictogram(cleaned_words)
    random_weighted_words = [get_random_word(listogram) for random_weighted_word in range(12)]
    sentence = generate_sentence(random_weighted_words)

    # print sentence
    print(sentence)