import re #regex expressions
import random
from sample import one_word
from dictogram import Dictogram

def cleanup(text):
    with open(text, 'r') as original_text:
        remove_periods = re.sub('(\s\.){4,}', '', original_text.read())
        new_text = re.sub('\*', '', remove_periods)
    return new_text

def tokenize(text):
    #Take the clean twilight txt file and make a very long list
    word_list = text.split()
    #return that list
    return word_list

def markov(text_list):
    #make a dictogram
    markov_dictogram = dict()
    #go through all the words except the last one
    for index in range(len(text_list)-1):
        #word, token, key
        word = text_list[index]
        # if we find that key
        if word in markov_dictogram:
            # increase value by 1
            markov_dictogram[word].add_count([text_list[index + 1]])
        else:
            # else add the key to the dictogram
            markov_dictogram[word] = Dictogram([text_list[index]])
    return markov_dictogram

def markov_order(order, text_list):
    # make a dictogram
    markov_dictogram = dict()
    for index in range(len(text_list) - order):
        window = tuple(text_list[index: index + order])
        if window in markov_dictogram:
            markov_dictogram[window].add_count(text_list[index + order])
        else:
            markov_dictogram[window] = Dictogram([text_list[index + order]])
    return markov_dictogram

def start_token(dictionary):
    start_tokens = []
    for key in dictionary:
        if key[0].islower() is False and key[0].endswith('.') is False:
            start_tokens.append(key)
    token = random.choice(start_tokens)
    return token

def stop_token(dictionary):
    stop_tokens = []
    for key, value in dictionary.items():
        if key[2].endswith('.') or key[2].endswith('?'):
            stop_tokens.append(key)
    return stop_tokens

def create_sentence(start_token, stop_tokens, dictionary):
    sentence = []
    (word1, word2, word3) = start_token
    sentence.append(word1)
    sentence.append(word2)
    sentence.append(word3)

    current_token = start_token
    while current_token not in stop_tokens or len(sentence) <= 8:
        for key, value in dictionary.items():
            if key == current_token:
                cumulative = sample.cumulative_distribution(value)
                sample_word = sample.sample(cumulative)
                sentence.append(sample_word)
                (current_token_one, current_token_two, current_token_three) = current_token
                current_token = (current_token_two, current_token_three, sample_word)
                break
    return sentence


def main(text_list):
    dictionary = order_markov(2, text_list)
    first_word = start_token(dictionary)
    end_words = stop_token(dictionary)
    markov_list = create_sentence(first_word, end_words, dictionary)
    markov_sentence = " ".join(markov_list)
    return markov_sentence

if __name__ == "__main__":
    source_text = 'twilight-short.txt'
    clean_text = cleanup(source_text)
    text_list = tokenize(clean_text)
    main(text_list)





if __name__ == "__main__":
    text = 'twilight-short.txt'
    clean_text = cleanup(text)
    # print(clean_text)
    word_tokens = tokenize(clean_text)
    print(word_tokens)
    # markov_pairs = markov(word_tokens)
    # print(markov_pairs)