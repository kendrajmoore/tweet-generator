import random
import sys

word = sys.argv[1:]
#word.remove(word[0])
new_words = []

def random_word():
    for x in range(0, len(word)):
        rand_index = random.randint(0, len(word) -1)
        new_words.append(word[rand_index])
        print(rand_index)
        word.pop(rand_index)


if __name__ == "__main__":
    word = random_word()
    # turn from list into string
    print(*new_words)