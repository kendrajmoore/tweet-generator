import sys
#list histogram
def list_words(file):
    f = open(file, "r")
    list = f.read().split()
    f.close()
    return list


def words_list(list):
    list.sort()
    new_list = []
    count  = 0
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

def unique_words_list(histogram):
    return len(histogram)


def frequency_list(histogram, word):
    word = word.lower()
    for i in histogram:
        print(histogram)
        if i[0] == word:
            return i[1]
        else: 
            return('Not found')

# def test_histogram():
#     #print listogram
#     params = sys.argv[1:]
#     file = params[0]
#     words = list_words(file)
#     list_dict = words_list(words)
#     print('Histogramz: {}'.format(list_dict))

def get_length():
    params = sys.argv[1:]
    file = params[0]
    words = list_words(file)
    list_dict = words_list(words)
    unique_keys = unique_words_list(list_dict)
    print(unique_keys)

def get_frequency():
    params = sys.argv[1:]
    file = params[0]
    word = params[1]
    words = list_words(file)
    list_dict = words_list(words)
    freq = frequency_list(list_dict, word)
    print(freq)



if __name__ == '__main__':
    #print listogram
    # test_histogram()
    #print listogram
    # uncomment to get length
    # get_length()
    # uncomment to get length
    get_frequency()