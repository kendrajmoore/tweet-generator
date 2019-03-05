import random

text = 'one fish two fish red fish blue fish'
word_list = text.split()
# print(word_list)

def histogram(word_list):
    """Builds histogram from text input"""
    dict = {}
    for word in word_list:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict

hist = histogram(word_list)
print(hist)

def weighted_random_select(dict):
    """Takes in a histogram and generates a random word with weighted probability"""
    random_choice = random.randint(1, sum(dict.values()))
    weights_sum = 0
    print(random_choice)

    for key in dict:
        weights_sum += dict[key]
        print(key, dict[key])
        print(weights_sum)

        if random_choice <= weights_sum:
            return key
            exit

def frequency_test(hist, word_list):
    """Takes in the histogram, runs the weighted random selection function on it to generate a list of relative probabilities associated with each word"""
    temp_word_list = []
    for i in range(100000):
        select_word = weighted_random_select(hist, word_list)
        temp_word_list.append(select_word)
    frequency_list = histogram(temp_word_list)
    for key in frequency_list:
        frequency_list[key] = frequency_list[key]/len(temp_word_list)
        # frequency_list[key] = frequency_list[key]

    print(frequency_list)



# frequency_test(hist, word_list)