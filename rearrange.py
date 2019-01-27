import random
import sys


word = sys.argv[1]
new_words = [];

def random_word():
    for i in word:
        """ because index starts at zero """
        rand_index = random.randit(0, len(word) - 1)
        """ put word in random location in new words list """
        new_words.append(word[rand_index])

if __name__ == '__main__':
    word = random_word()
    print(new_words)