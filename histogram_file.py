import sys
from dictionary_histograms import words_dict 


def list_words(file):
    f = open(file, "r")
    list = f.read().split()
    f.close()
    return list

def histogram_file(list, words_dict):
    text_file.write('\n********RESULTS*********')
    for key, value in words_dict.items():
        text_file.write('{} : {}\n'.format(key, value))
    
