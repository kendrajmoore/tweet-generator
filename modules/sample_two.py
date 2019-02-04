import sys
import random
from dictionary_histograms import words_dict 
from list_histograms import words_list


"""Your first task is to write a function that takes a histogram (however you've structured yours)
and returns a single word, at random. It should not yet take into account the distributions of 
the words. """

def one_word(histogram):
    histogram = list(histogram.keys())
    print(str(histogram[random.randint(0, len(histogram) -1)]))

"""Once you have that working, can you prove that your code is truly random?
 Granted, proving randomness is much more difficult than disproving it, 
 but you can get close. Is the probability that any word is selected the 
 same as for any other word?  """

def list_words(file):
    f = open(file, "r")
    list = f.read().split()
    f.close()
    return list

def weighted_list(list):
    weights = []
    for word in list:
        word_count = list.count(word)
        weight = word_count/len(list)
    weights.append(word_count)
    weights_and_count = zip(list, weights)
    weights_count_list = list(weights_and_count)


def word_probability(weighted_histogram, num_trials):
    results = []
    for i in range(num_trials):
        not_chosen = True
        while not_chosen:
            random.choice = random.choice(weighted_histogram)
            word, probability = random_choice
            random_number = random.uniform(0, 1)
            if probability > random_number:
                results.append(word)
                not_chosen = False
            else:
                continue
    return results

def logger(file_name, histogram):
    f = open(file_name, "a")
    f.write("\n\n{}".format(histogram))




if __name__ in '__main__':
    #part-one
    # args = sys.argv[1:]
    # histogram = words_dict(args)
    # one_word(histogram)
    #end-part-one
    params = sys.argv[1:]
    file = params[0]
    words_list = list_words(file)
   
    
    