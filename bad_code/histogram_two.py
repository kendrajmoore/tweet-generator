"""A histogram() function which takes a source_text argument (can be either a filename 
or the contents of the file as a string, your choice) and return a histogram data structure
that stores each unique word along with the number of times the word appears in the source 
text. A unique_words() function that takes a histogram argument and returns the total count 
of unique words in the histogram. For example, when given the histogram for The Adventures 
of Sherlock Holmes, it returns the integer 8475.
A frequency() function that takes a word and histogram argument and returns the number of 
times that word appears in a text. For example, when given the word "mystery" and the 
Holmes histogram, it will return the integer 20."""


import sys

def histogram(source_text):
    #read my twilight file
    f = open(source_text, "r")
    #puts text in a list of strings
    words = f.read().split()
    # for my personal happiness
    words_sorted = sorted(words)
    f.close()
    #remove all of these extras
    remove_punc = '.,-_'
    #make a dictionary
    wordDict = {}
    #for loop
    for word in words_sorted:
        #remove punc
        clean_word = word.strip(remove_punc)
        #add word and count
        if clean_word not in wordDict:
            wordDict[clean_word] = 0
        # plus one if already in there
        wordDict[clean_word] += 1
    return wordDict





def unique_words(histogram):
    pass


def frequency(word, histogram):
    pass

if __name__ == '__main__':
    source_text = str(sys.argv[1])
    words = histogram(source_text)