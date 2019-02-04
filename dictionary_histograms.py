import sys
import string

def list_words(file):
    f = open(file, "r")
    list = f.read().split()
    f.close()
    return list

##dictionary histogram

def words_dict(list):
    my_dict = {}
    for word in list:
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] += 1
    return my_dict 

def unique_words_dict(histogram):
    print(len(histogram.keys()))

def freq_dict(histogram, word):
    word = word.lower()
    if word in histogram:
        return histogram[word]
    else:
        return str(0)

# def test_histogram():
    #uncomment to make histogram from twilight or one fish text.
    # params = sys.argv[1:]
    # file = params[0]
    # words_list = list_words(file)
    # dict = words_dict(words_list)
    # print('Histogramz: {}'.format(dict))

# def get_length():
#     #uncomment to get unique keys
#     params = sys.argv[1:]
#     file = params[0]
#     words_list = list_words(file)
#     dict = words_dict(words_list)
#     unique_keys = unique_words_dict(dict)

def get_frequency():
    params = sys.argv[1:]
    file = params[0]
    word = params[1] 
    words_list = list_words(file)
    dict = words_dict(words_list)
    frequency = freq_dict(dict, word)
    print(frequency)





if __name__ == '__main__':
    #uncomment for histogram
    # test_histogram()
    #uncomment for histogram
    #uncomment to get unique keys
    # get_length()
    #uncomment to get unique keys
    get_frequency()