import sys
import random
from dictionary_histograms import wordsDict



"""Your first task is to write a function that takes a histogram (however you've structured yours) and returns
 a single word, at random. It should not yet take into account the distributions of the words. """

def one_word(histogram):
    histogram = list(histogram.keys())
    print(str(histogram[random.randint(0, len(histogram) -1)]))


if __name__ == '__main__':
    args = sys.argv[1:]
    