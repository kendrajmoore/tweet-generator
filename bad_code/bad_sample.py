# def one_word(histogram):
#     """Takes in a histogram made of dictionaries and returns a random word """
#     histogram = list(histogram.keys())
#     return str(histogram[random.randint(0, len(histogram) -1)])

# def weighted_word(histogram):
#     my_dict = {}
#     histogram_keys = list(histogram.keys())
#     histogram_values = list(histogram.values())
#     highest_frequency = 0
#     for i, value in enumerate(histogram_values):
#         if value not in my_dict:
#             my_dict[value] = histogram_keys[i]
#             if value > highest_frequency:
#                 highest_frequency = value
#         else:
#             my_dict[value].append(histogram_keys[i])
#     chance = random.uniform(0, highest_frequency / len(histogram_values))
#     histogram_values = sort

# import sys
# import random

# # word_list  = "one fish two fish green fish blue fish".split()

# """Your first task is to write a function that takes a histogram (however you've structured yours)
# and returns a single word, at random. It should not yet take into account the distributions of 
# the words. """

# def one_word():
#     """Take in a string from the command line, create histogram, and return one word """
#     histo = {}
#     #make a weighted histogram based on word frequency
#     for word in word_list: 
#         if word in histo.keys():
#             histo[word] += 1
#         else:
#             histo[word] = 1

#     count = 0
#     random_number = random.random()
#     for key, value in histo.items():
#         count += (value /len(word_list))
#         if count >= random_number:
#             return key


# # """Once you have that working, can you prove that your code is truly random?
# #  Granted, proving randomness is much more difficult than disproving it, 
# #  but you can get close. Is the probability that any word is selected the 
# #  same as for any other word?  """

# # def weighted_list(histogram):
# #     """ Prove truly random """
# #     count = 0
# #     #Return the next random floating point number in the range [0.0, 1.0).
# #     random_number = random.random()
# #     #method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
# #     for key, value in histogram.items():
# #         count += (value / len(params))
# #         if count >= random_number:
# #             return key