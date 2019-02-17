import sys
import random
from histogram import list_words
from histogram import histogram

def one_word(histogram):
    "takes in a histogram and returns a random word"
    histogram = list(histogram.keys())
    return str(histogram[random.randint(0, len(histogram)-1)])

def sort_array(array):
    "takes in an array and use sort method to sort it"
    return sorted(array)

def weighted(histogram):
    "takes in a histogram and returns word probability"
    my_dict = {}
    histogram_keys = list(histogram.keys())
    histogram_values = list(histogram.values())
    highest_frequency = 0
    for i, value in enumerate(histogram_values):
        if value not in my_dict:
            my_dict[value] = [histogram_keys[i]]
            if value > highest_frequency:
                highest_frequency = value
        else:
            my_dict[value].append(histogram_keys[i])
    chance = random.uniform(0, highest_frequency / len(histogram_values))
    histogram_values = sort_array(histogram_values)
    for value in histogram_values:
        if value / len(histogram_values) >= chance:
            return my_dict[value][random.randint(0, len(my_dict[value])-1)]



# def test():
#     histogram = {}
#     for i in range(0, 10000):
#         word = one_word()
#         if word in histogram:
#             histogram[word] += 1
#         else:
#             histogram[word] = 1
#     return histogram



if __name__ in '__main__':
    params = sys.argv[1:]
    file = params[0]
    words_list = list_words(file)
    gram = histogram(words_list)
    probability = weighted(gram)
    print(probability)
    




    