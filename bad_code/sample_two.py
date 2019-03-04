import sys
import random
import tokenize
import cleanup
import histogram
# from histogram import list_words
# from histogram import histogram

def one_word(gram):
    "takes in a histogram and returns a random word"
    # gram = list(histogram.keys())
    # print(gram)
    # return str(gram[random.randint(0, len(gram)-1)])
    histogram_type = str(type(gram).__name__ )
    if(histogram_type == "Listogram"):
        histogram = gram
    elif(histogram_type == "Dictogram"):
        histogram = [(key, value) for key, value in gram.items()]
    else:
        return

    total_words = gram.tokens

    words, counts = zip(*histogram)

    weights = [count/total_words for count in counts]

    random_word = ''
    while random_word == '':
        random_index = random.randrange(len(words))
        if random.random() < weights[random_index]:
            random_word = words[random_index]

    # return random word
    return random_word

# def sort_array(array):
#     "takes in an array and use sort method to sort it"
#     return sorted(array)

# def weighted(histogram):
#     "takes in a histogram and returns word probability"
#     my_dict = {}
#     histogram_keys = list(histogram.keys())
#     histogram_values = list(histogram.values())
#     highest_frequency = 0
#     for i, value in enumerate(histogram_values):
#         if value not in my_dict:
#             my_dict[value] = [histogram_keys[i]]
#             if value > highest_frequency:
#                 highest_frequency = value
#         else:
#             my_dict[value].append(histogram_keys[i])
#     chance = random.uniform(0, highest_frequency / len(histogram_values))
#     histogram_values = sort_array(histogram_values)
#     for value in histogram_values:
#         if value / len(histogram_values) >= chance:
#             return my_dict[value][random.randint(0, len(my_dict[value])-1)]



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
    word = words_list(file)
    clean_word = cleanup(word)
    listogram = Dictogram(clean_word)
    random_weighted_word = one_word(listogram)
    print(random_weighted_word)

    # #list words
    # words_list = list_words(file)
    # #histogram
    # grams = histogram(words_list)
    # #print single word
    # random_word = one_word(grams)
    # probability = weighted(grams)
    # print(probability)
    




    