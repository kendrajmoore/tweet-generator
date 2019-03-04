import string

def cleanup(words):
    "Takes in a list of words and removes punctuation "
    #takes that list and removes spaces, punc, and numbers
    #this is not working well
    translation = str.maketrans('', '', '''!"#$%&()*+,./:;<=>?@[\]^_`{|}~`1234567890''')
    # print(translation)
    words[:] = [i.replace(' ', '') for e in words for i in e.split('--')]
    # print(words)
    letters = [i + '.' for i in string.ascii_uppercase]
    # print(letters)
    letter_words = ['a', 'i']
    # print(letter_words)
    abbreviations3 = ['dr.', 'mr.']
    abbreviations4 = ['mrs.', 'ms.']
    words[:] = [i for i in words if i[-2:] not in letters and
                i[-3:].lower() not in abbreviations3 and
                i[-4:].lower() not in abbreviations4 and
                not (len(i) == 1 and i.lower() not in
                        letter_words)]
    words[:] = [i.translate(translation).lower().lstrip(
        "'").rstrip("'") for i in words]
    
    return words



if __name__ == "__main__":
    import sys
    from tokenize import words_list
    words = words_list(sys.argv[1])
    clean_corpus = cleanup(words)
    # print(clean_corpus)

    for word in clean_corpus:
        print(word)