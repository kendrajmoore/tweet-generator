import sys

def list_words(file):
    f = open(file, "r")
    list = f.read().split()
    f.close()
    return list

def remove_punc(list):
    punctuation = ["@" , "#" , "$" , ":", ";", "_", "*" , "}" , "[" , "{" , "]" , "," , ".", "!" , "?"]
    for i, word in enumerate(list):
        new_word = ''
        for char in word:
            if char not in punctuation:
                new_word += char
        list[i] = new_word
        return list


def lower_list(list):
    list = [x.lower() for x in list]
    return list


def words_tuples(list):
    list.sort()
    list = []
    count = 0
    index = None
    for word in list:
        if word == index:
            count += 1
        else:
            list.append((index, count))
            index = word
            count = 1
    else:
        list.append((index, count))
        list.pop(0)
    return list

def unique_words_tuples(histogram):
    return len(histogram)

def frequency_tuples(histogram, word):
    word = word.lower()
    for entry in histogram:
        if entry[0] == word:
            return entry[1]
    else:
        return('Not found')

def test_histogram():
    params = sys.argv[1:]
    file = params[0]
    words_list = words_tuples(list)
    print('Histogramz: {}'.format(words_list))


if __name__ == '__main__':
    
    # print('file: {}'.format(file))
    # print((wordsDict(lowerList(remove_punc(listWords(file))))))
    
    # print((wordsDict(lowerList(remove_punc(listWords(file))))))
    test_histogram()