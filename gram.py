import sys


def list_words(file):
    """Open a file and turn the text into a list """
    with open(file, 'r') as f:
        list = f.read().split()
    return list

def histogram():
    """ Take a file and return a dictionary histogram """
    histogram = {}

    list = list_words()

    for word in list:
        # if word not in histogram
        if histogram.get(word) == None:
            histogram[word] = 1
        else:
            histogram[word] += 1

    return histogram


def histogram_list():
    """ Take the file and return a histogram of lists """
    new_list = []

    list = list_words()
    list.sort()
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
    return new_list


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    word = word.lower()
    for entry in histogram:
        if entry[0] == word:
            return entry[1]
        else:
            return('Not found')
    


if __name__ == '__main__':
    print(histogram())
    # print(histogram_list0flist())
    # print(histogram_listList())

    # print(histogram_listOfTuples())
    # print(histogram_listTuples())

    # print(unique_words(histogram()))
    # print(frequency('Forks', histogram()))