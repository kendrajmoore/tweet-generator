import sys

def listWords(file):
    f = open(file, "r")
    list = f.read().split()
    f.close()
    return list

def remove_punc(list):
    punctuation = ["@" , "#" , "$" , ":", ";", "_", "*" , "}" , "[" , "{" , "]" , "," , ".", "!" , "?"]
    for i, word in enumerate(list):
        newWord = ''
        for char in word:
            if char not in punctuation:
                newWord += char
        list[i] = newWord
        return list

def lowerList(list):
    list = [x.lower() for x in list]
    return list

##dictionary histogram

def wordsDict(list):
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
## list of list histogram

def wordsList(list):
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
    return list

def unique_wordsList(histogram):
    return len(histogram)


def frequencyList(histogram, word):
    word = word.lower()
    for entry in histogram:
        if entry[0] == word:
            return entry[1]
        else: 
            return('Not found')


#list of tuples histogram

def wordsTuples(list):
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

def unique_wordsTuples(histogram):
    return len(histogram)

def frequencyTuples(histogram, word):
    word = word.lower()
    for entry in histogram:
        if entry[0] == word:
            return entry[1]
    else:
        return('Not found')

if __name__ == '__main__':
    file = str(sys.argv[1])
    print((wordsDict(lowerList(remove_punc(listWords(file))))))