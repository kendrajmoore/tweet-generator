from collections import deque
import sys
import string
import random


if __name__ == '__main__':
        file = str(sys.argv[1])
        word = sys.argv[2]  #stringify here
        n = sys.argv[3]     #and here
        #run()

def arrayFileWords(file):
    """opens a file, puts the words into an array,
    closes the file and returns the array of strings"""
    f = open(file, "r")
    array = f.read().split()
    f.close()
    return array

def strip_Punc(array):
    """opens an array of strings, cycles through each word and then each character
    of a word and replaces that word with an exact copy but without punctuation. returns the array."""
    punctuation = ["@" , "#" , "$" , ":", ";", "_", "*" , "}" , "[" , "{" , "]"]
    #, "," , ".", "!" , "?"] #took out single and double quotes from this array
    for i, word in enumerate(array):
        newWord = ""
        for char in word:
            if char not in punctuation:
                newWord += char
        array[i] = newWord
    return array

def lowercaseArray(array):
    """takes in an array of strings, uses a list comprehension to lowercase each letter"""
    uppercase = ["I", "\'I" , "\"I"]
    array = [x.lower() for x in array if x not in uppercase and x not in propers]
    return array

def lowercase_Array(array):
    newArray = []
    uppercase = ["I", "\'I" , "\"I"]
    for word in array:
        if word in uppercase or word in propers:
            newArray.append(word)
        else:
            newArray.append(word.lower())
    return newArray

def arrayToString(array):
    """takes in an array and returns the a string of the elements separated by spaces"""
    string = ""
    for elem in array:
        string += str(elem)
    return string

def uppercaseWords(string):
    next = False
    punctuation = ["." , "!" , "?"]
    array = []
    for char in string:
        array.append(char)
    for i, element in enumerate(array):
        #print(array[i-2])
        if next == True:
            array[i] = element.upper()
            next = False
        elif array[i-2] in punctuation and i > 2:
            if element != "\'" and element != "\"":
                print((True, str(element)))
                array[i] = element.upper()
            else:
                next = True
    return array


def lookForProper(array):
    propers = []
    noproper = []
    for word in array:
        for i, char in enumerate(word):
            if i == 0 and char.islower() and word.title() in propers:
                propers.remove(word.title())
                noproper.append(word)
            if char.istitle() and word not in propers and word not in noproper:
                propers.append(word)
    return propers


#def removeSpaces(array):
#    array = [array.pop(i) for i, x in enumerate(array) if x == " "]

def wordBeforeAfter(array):
    """takes in an array of strings,
    using the global variables word and n,
    looks for instances of the word in the array.
    if an instance of the word is found,
    compiles an array of n words that come before the word.
    returns an array of tuples of
    (1) instance of word,
    (2) array of n words before the instance of the searched word, and
    (3) the next word that comes after the instance of the searched word."""
    instances = []
    for i, fileWord in enumerate(array):
        if fileWord == str.lower(str(word)):
            x = i -1
            beforeWords = []
            #while x > (i - int(n) - 1): #if you want n words before word
            while x > (i - int(n)): #if you want n words after next-word
                beforeWords.append(array[x])
                x -= 1
            myTuple = (word, beforeWords, array[i+1])
            instances.append(myTuple)
    return instances

def firstOrderMarkov(arrayOfTuples):
    """takes in an array of tuples of (word, [array of words before word], next word that comes after word)
    creates a dictionary of {next word : number of instances}. splits the dictionary into a 'twin index' of two arrays: keys and values.
    "twin index" = keys[0] and values[0] reference the key and value pair of the dictionary that was 'split'.
    for each key the function prints to console what the likelihood is of that key appearing as the next word."""
    myDict = {}
    for i, instance in enumerate(arrayOfTuples):
        if instance[2] not in myDict:
            myDict[arrayOfTuples[i][2]] = 1
        else:
            myDict[arrayOfTuples[i][2]] += 1
    keys = list(myDict.keys())
    values = list(myDict.values())
    print(keys)
    print(values)

def nOrderMarkov(instances):
    """takes in an array of tuples (word, [array of n words before word], and next word),
    cycles through the array of tuples and appends the next word and the word to an array,
    and then appends the array of before words
    NEED TO EDIT DOCSTRING..."""
    arrayofArrays = []
    myDict = {}
    for i, instance in enumerate(instances):
        myArray = [] #array in "backwards" chronological order from last word (next) to first word
        myArray.append(instance[2]) #next word
        myArray.append(instance[0]) #word
        myArray+=instance[1] #array of words before word
        arrayofArrays.append(myArray)
    for array in arrayofArrays:
        if tuple(array) not in myDict:
            myDict[tuple(array)] = 1
        else:
            myDict[tuple(array)] += 1
    keys = list(myDict.keys())
    values = list(myDict.values())
    return(keys, values)

def checkChars(myTweet):
    """checks to see how many characters there are in myTweet. if there are less
    than 140 then it returns True."""
    punctuation = [".", "!" , "?"]
    counter = 0
    period = False
    for chars in myTweet:
        counter += 1
        if counter > 140 and chars in punctuation:
            period = True
        elif counter > 300:
            period = True
    if period == False:
        return True
    else:
        return False
    #and chars in punctuation:
        #    period = True
    #if period == True:
    #    return True
    #else:

n = 6
file = "twilight.txt"
words = arrayFileWords(file)
word = arrayFileWords(file)[random.randint(0, len(words)-1)]
myTweet = str(word)
upperRange = int(n)                          #creates variety
lowerRange = (int(n) - (int(n)//1.5))        #consider changing
if lowerRange < 1:
    lowerRange = 1
exception = True
keysValues = nOrderMarkov(wordBeforeAfter(strip_Punc(arrayFileWords(file))))
while checkChars(myTweet) and exception:
    try:

        #arrayWords = arrayFileWords(file)
        #propers = lookForProper(arrayWords)
        #keysValues = nOrderMarkov(wordBeforeAfter(strip_Punc(lowercase_Array(arrayWords))))
        x = 0
        storeIndex = []
        for i, value in enumerate(keysValues[1]):
            if value > x:                         #right now it is just going to the highest frequency word, use herd_immunity virus_repro-style
                x = value
                storeIndex.append(i)
                word = keysValues[0][storeIndex[random.randint(((len(storeIndex)-1)//2), (len(storeIndex)-1))]][0]       #i could check to see if the word is in the sentence, would completely get rid of repeats tho...
                n = random.randint(lowerRange, upperRange)#i could check to see if the chars in the word match the up with the last 20 chars, if so use next most frequent word
                #print(len(storeIndex))
                myTweet += str(n)                            #maybe use a queue to do first in, first out of words or chars to consistently check; repetition of the same word is killing me
                myTweet += " "
                myTweet += word
                checkChars(myTweet)
    except:
        exception = False
else:
    print(arrayToString(uppercaseWords(myTweet)))
    print(lowerRange)
    print(upperRange)