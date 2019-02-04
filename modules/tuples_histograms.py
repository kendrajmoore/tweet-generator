import sys

def list_words(file):
    f = open(file, "r")
    list = f.read().split()
    f.close()
    return list


def words_tuples(list):
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
    return new_list

def unique_words_tuples(histogram):
    return len(histogram)

def frequency_tuples(histogram, word):
    word = word.lower()
    for entry in histogram:
        if entry[0] == word:
            return entry[1]
    else:
        return('Not found')

# def test_histogram():
#     params = sys.argv[1:]
#     file = params[0]
#     words_list = list_words(file)
#     tuple = words_tuples(words_list)
#     print('Histogramz: {}'.format(tuple))

# def get_length():
#     params = sys.argv[1:]
#     file = params[0]
#     words_list = list_words(file)
#     tuple = words_tuples(words_list)
#     unique_keys = unique_words_tuples(tuple)
#     print(unique_keys)

def get_frequency():
    params = sys.argv[1:]
    file = params[0]
    word = params[1]
    words_list = list_words(file)
    tuple = words_tuples(words_list)
    freq = frequency_tuples(tuple, word)
    print(freq)


if __name__ == '__main__':
    # #for histogram
    # test_histogram()
    # #for histogram
    # get_length()
    get_frequency()