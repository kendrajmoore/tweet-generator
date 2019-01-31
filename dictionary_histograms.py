import sys
import string

def listWords(file):
    f = open(file, "r")
    list = f.read().split()
    f.close()
    return list

#not working
def remove_punc(list):
    pass
    # translator = str.maketrans("@" , "#" , "$" , ":", ";", "_", "*" , "}" , "[" , "{" , "]" , "," , ".", "!" , "?")

#not working

def lowerList(list):
    list = [x.lower() for x in list]
    return list

##dictionary histogram

def words_dict(list):
    myDict = {}
    for word in list:
        if word not in myDict:
            myDict[word] = 1
        else:
            myDict[word] += 1
    return myDict 

def unique_wordsDict(histogram):
    return len(histogram.keys())

def freqDict(histogram, word):
    word = word.lower()
    if word in histogram:
        return histogram[word]
    else:
        return str(0)

def test_histogram():
    params = sys.argv[1:]

    file = params[0]
    words_list = listWords(file)
    clean_list = remove_punc(words_list)
    lower_case_list = lowerList(clean_list)
    dict = words_dict(lower_case_list)
    print('Histogramz: {}'.format(dict))

if __name__ == '__main__':
    
    # print('file: {}'.format(file))
    # print((wordsDict(lowerList(remove_punc(listWords(file))))))
    
    # print((wordsDict(lowerList(remove_punc(listWords(file))))))
    test_histogram()