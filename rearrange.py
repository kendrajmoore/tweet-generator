import random
import sys

word = sys.argv
word.remove(word[0])
new_words = []

def random_word():
    for x in word:
        rand_index = random.randint(0, len(word) - 1)
        new_words.append(word[rand_index])


if __name__ == '__main__':
    word = random_word()
    print(new_words)