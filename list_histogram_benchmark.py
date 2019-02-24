import sys
import string
import timeit


def list_words():
    """Open a file and turn the text into a list """
    dict_words = '/usr/share/dict/words'
    with open(dict_words, 'r') as f:
       list = f.read().split("\n")
    return list


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
    return new_list


def find(item, new_list):
    for index, pair in enumerate(new_list):
        if pair[0] == item:
            return index
    return None

def list_of_words(list_words, length):
    return list[0:length]

def count(word, new_list):
    index = find(word, new_list)
    if index:
        word_count_pair = new_list[index]
        return word_count_pair[1]
    else:
        return 0

if __name__ == "__main__":
     #benchmark
    hundred_words       = list_of_words(100)
    ten_thousand_words  = list_of_words(10000)

    hundred_hgram       = histogram_list(hundred_words)
    ten_thousand_hgram  = histogram_list(ten_thousand_words)

    hundred_search      = hundred_words[-1]
    ten_thousand_search = ten_thousand_words[-1]

    # stmt  = "count('{}', hundred_hgram)".format(hundred_search)
    # setup = "from __main__ import count, hundred_hgram"
    # timer = timeit.Timer(stmt, setup=setup)

    stmt  = "count('{}', ten_thousand_hgram)".format(ten_thousand_search)
    setup = "from __main__ import count, ten_thousand_hgram"
    timer = timeit.Timer(stmt, setup=setup)

    # iterations = 10000
    # result = timer.timeit(number=iterations)
    # print("count time for 100-word histogram: " + str(result))

    iterations = 10000
    result = timer.timeit(number=iterations)
    print("count time for 10000-word histogram: " + str(result))



if __name__ == "__main__":
    lists = list_words()
    gram = histogram_list(lists)
    # print(gram)
    find_bool = find('aal', gram) == 3
    print(find_bool)
