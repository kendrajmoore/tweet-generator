import sys
import re
import random
#step one

def cleanup(file):
    words = open(file, 'r').read().lower()
    # print(words)
    remove_periods = re.sub(r"\." , " STOP START ", words)
    # print(remove_periods)
    remove_punctuation = re.sub(r"\W", " " , remove_periods)
    # print(remove_punctuation)
    word_list = remove_punctuation.split()
    # print(word_list)
    if word_list[(len(word_list)-1)] == 'START':
        word_list.pop()
    if word_list[0] != 'START':
        word_list.insert(0, 'START')
    return word_list

if __name__ == "__main__":
    params = sys.argv[1:]
    file = params[0]
    texts = cleanup(file)
    print(texts)
   
