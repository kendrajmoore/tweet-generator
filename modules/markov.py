import sys 
import cleanup
import sample
import sentence
import dictogram
import random

def markov(list):
    markov_dict = {}
    for index in range(len(list) - 1):
        word = list[index]
        if index in markov_dict:
            markov_dict[words].add_count([list[index + 1]])
        else:
            markov_dict[words] = dictogram.Dictogram([list[index + 1]])
    return markov_dict

    def markov_norder(order, list):
        markov_dict = {}
        for index in range(len(list) - order):
            word = tuple(list[index: index + order])
            if word in markov_dict:
                markov_dict[words].add_count([list[index + order]])
            else:
                markov_dict[words] = dictogram.Dictogram([list[index + order]])
        return markov_dict

def start_token(model):
    start_tokens = []
    for key in model:
        if key[0] == "START":
            start_tokens.append(key)
    token = random.choice(start_tokens)
    return token

def stop_tokens(dict):
    stop_tokens = []
    for key, value in dict.items():
        if key[1] == 'STOP':
            stop_tokens.append(key)
    return stop_tokens

def walk(start_token, dict):
    sentence = ['START', start_token[1]]
    while sentence[len(sentence) -1] != 'STOP':
        words = (sentence[len(sentence) - 2], sentence[len(sentence)-1])
        hist = dict[tuple(words)]
        next_word = sample.weighted_random(hist, sample.sum_value(hist))
        sentence.append(next_word)
    return sentence

def final(sentence):
    sentence.pop(0)
    sentence.pop()
    sentence[0] = sentence[0].capitalize()
    word_string = ''
    word_string = word_string.join(' '+ word for word in sentence) + '.'
    return word_string






if __name__ == '__main__':
    params = sys.argv[1:]
    file = params[0]
    words = cleanup.cleanup(file)
    # histo = tweet_histogram.dictogram_words(words)
    # file1 = argv[1]  #file to analyze
    # words = cleanup.cleanup(file1)
    # m_chain = markov(2, words)
    m_chain = markov(words)
    print(m_chain)
    # c_start = start_token(m_chain)
    # walk_the_dog = walk(c_start, m_chain)
    # print(finalize(walk_the_dog))

