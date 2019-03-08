from dictogram import Dictogram
from cleanup import get_word_list
from sample import weighted_random_select
import sys, random

# dict[word] = 1

def dict_of_hists_entry(select_word, word_list):
    words_after_list = []
    for index in range(len(word_list)-1):
        if select_word == word_list[index]:
            words_after_list.append(word_list[index+1])
    select_word_hist = Dictogram(words_after_list)
    return select_word_hist

def dict_of_hists(histogram, word_list):
    master_dict = {}
    for word in histogram:
        entry = dict_of_hists_entry(word, word_list)
        master_dict[word] = entry
    return master_dict

def new_word(word_select, master_histogram):
    # random_choice = random.randint(0, len(word_list) - 1)
    # word_select = word_list[random_choice]
    entry = master_histogram[word_select]
    new_word = weighted_random_select(entry)
    return new_word

def sentence(word_list, master_histogram, sen_length = 10):
    sentence = []
    random_choice = random.randint(0, len(word_list) - 1)
    word_select = word_list[random_choice]
    sentence.append(word_select)
    for i in range(sen_length):
        word = new_word(word_select, master_histogram)
        sentence.append(word)
        word_select = word
    print(*sentence)
    return sentence

if __name__ == '__main__':
    if len(sys.argv) == 2:
        word_list = get_word_list(sys.argv[1])
    else:
        word_list = get_word_list()
    histogram = Dictogram(word_list)
    master_dict = dict_of_hists(histogram, word_list)
    sentence(word_list, master_dict, 15)
    # if len(sys.argv) == 3:
    #     sentence(word_list, master_dict, sys.argv[3])
    # else:
    #     sentence(word_list, master_dict)
