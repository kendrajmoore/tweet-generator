import sys
import random

word_list  = "one fish two fish green fish blue fish".split()

"""Your first task is to write a function that takes a histogram (however you've structured yours)
and returns a single word, at random. It should not yet take into account the distributions of 
the words. """

def one_word():
    """Take in a string from the command line, create histogram, and return one word """
    histo = {}
    for word in word_list: 
        if word in histo.keys():
            histo[word] += 1
        else:
            histo[word] = 1

    count = 0
    random_number = random.random()
    for key, value in histo.items():
        count += (value /len(word_list))
        if count >= random_number:
            return key


# """Once you have that working, can you prove that your code is truly random?
#  Granted, proving randomness is much more difficult than disproving it, 
#  but you can get close. Is the probability that any word is selected the 
#  same as for any other word?  """

# def weighted_list(histogram):
#     """ Prove truly random """
#     count = 0
#     #Return the next random floating point number in the range [0.0, 1.0).
#     random_number = random.random()
#     #method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
#     for key, value in histogram.items():
#         count += (value / len(params))
#         if count >= random_number:
#             return key

def test():
    histogram = {}
    for i in range(0, 10000):
        word = one_word()
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram



if __name__ in '__main__':
    #part-one
    print(one_word())
    print(test())



    