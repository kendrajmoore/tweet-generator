import sys
import string


def list_words(file):
    """Open a file and turn the text into a list """
    with open(file, 'r') as f:
       list = f.read().split()
    return list

def histogram(list):
    """ Take a file and return a dictionary histogram """
    histogram = {}

    for word in list:
        # if word not in histogram
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1

    return histogram


def histogram_list(list):
    """ Take the file and return a histogram of lists """
    list.sort()
    new_list = []
    count = 0
    index = None
    for word in list:
        if word == index:
            count += 1
        else:
            new_list.append([index, count])
            index = word
            count = 1
    else:
        new_list.append([index, count])
        list.pop(0)
    print(new_list)



def histogram_tuples(list):
    """ Take in a list and turn it into one long list of tuples """
    # using the dictionary to add the items in the tuple
    list.sort()
    new_list = []
    count = 0
    index = None
    for word in list:
        if word == index:
            count += 1
        else:
            new_list.append((index, count))
            index = word
            count = 1
    else:
        new_list.append((index, count))
        new_list.pop(0)
    print(new_list)


def unique_words(histogram):
    print(len(histogram))


def frequency_list(histogram, word):
    word = word.lower()
    for i in histogram:
        if i[0] == word:
            return i[1]
        else: 
            return('Not found')
    


if __name__ == '__main__':
    params = sys.argv[1:]
    file = params[0]
    
    # part-one
    words_list = list_words(file)
    dict = histogram(words_list)
    #  part-one
  
    # part-two
    # words_list = list_words(file)
    list_hist = histogram_list(words_list)
    print(list_hist)
    # part-two

    # words_list = list_words(file)
    # tuple_gram = histogram_tuples(words_list)

    # words = unique_words(dict)
    word = params[1]
    freq = frequency_list(list_hist, word)
    print(freq)
