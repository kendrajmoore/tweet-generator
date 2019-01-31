import sys
import random
from dictionary_histograms import words_dict



"""Your first task is to write a function that takes a histogram (however you've structured yours) and returns
 a single word, at random. It should not yet take into account the distributions of the words. """

def one_word(histogram):
    histogram = list(histogram.keys())
    print(str(histogram[random.randint(0, len(histogram) -1)]))


def weighted_histogram(histogram):
    pass

    
if __name__ == '__main__':
    args = sys.argv[1:]
    histogram = words_dict(args) # Take in words and create a histogram
    one_word(histogram)

    