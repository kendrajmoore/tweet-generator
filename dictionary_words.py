
import random
import sys
import timeit

"""The program only accepts one argument: the number of words to be selected.
All parameters except the number of words will be hard-coded.
We will use the words file which is available on all Unix systems for our list of words.
The sentences do not have to make grammatical sense.
Word selection can be completely random and the word order does not matter."""


def file():
    #should rename this function because not returning a file
    f = open("/usr/share/dict/words", "r")
    words = f.read().split()
    f.close()
    return words


def dictionary(number):
    wordsList = []
    x = 0

    while x < number:
        # i was using this wrong in rearrange.py
        wordsList.append(words[random.randint(0, (len(words) - 1))])
        x += 1
    print(*wordsList)
  
    

if __name__ == '__main__':
    number = sys.argv[1]
    number = int(number)
    words = file()
    list = (dictionary(number))
    