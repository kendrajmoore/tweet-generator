import sys
import random
from histogram import histogram 
from histogram import list_words


"""Your first task is to write a function that takes a histogram (however you've structured yours)
and returns a single word, at random. It should not yet take into account the distributions of 
the words. """

def one_word(histogram):
    """Take in a string from the command line, create histogram, and return one word """
    histogram = list(histogram.keys())
    return str(histogram[random.randint(0, len(histogram) -1)])

"""Once you have that working, can you prove that your code is truly random?
 Granted, proving randomness is much more difficult than disproving it, 
 but you can get close. Is the probability that any word is selected the 
 same as for any other word?  """

def weighted_list(histogram):
    """ Prove truly random """
    count = 0
    #Return the next random floating point number in the range [0.0, 1.0).
    random_number = random.random()
    #method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
    for key, value in histogram.items():
        count += (value / len(params))
        if count >= random_number:
            return key

def test(histogram):
    for i in range(0, 10000):
        word = one_word(histogram)
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram



if __name__ in '__main__':
    #part-one
    params = sys.argv[1:]
    histogramz = histogram(params)
    # print(one_word(histogramz))
    #end-part-one
    #part-two
    # params = sys.argv[1:]
    # histogramz = histogram(params)
    # weights = weighted_list(histogramz)
    # print(weights)
    #part-two
    probability = test(histogramz)
    print(probability)



   
    
    