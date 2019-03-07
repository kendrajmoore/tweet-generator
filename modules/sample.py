import random
import sys

def list_words(file):
    """Open a file and turn the text into a list """
    with open(file, 'r') as f:
       list = f.read().split()
    return list


def histogram(word_list):
    dict = {}
    for word in word_list:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict



def weighted_sample(dict):
    word_choice = random.randint(1, sum(dict.values()))
    weights = 0
    for key in dict:
        weights += dict[key]
        if word_choice <= weights:
            return key


def frequency_test(hist, list):
    """Takes in the histogram, runs the weighted random selection function on it to generate a list of relative probabilities associated with each word"""
    temp_word_list = []
    for i in range(100000):
        select_word = weighted_sample(hist, list)
        temp_word_list.append(select_word)
    frequency_list = histogram(temp_word_list)
    for key in frequency_list:
        frequency_list[key] = frequency_list[key]/len(temp_word_list)
        # frequency_list[key] = frequency_list[key]

    print(frequency_list)

