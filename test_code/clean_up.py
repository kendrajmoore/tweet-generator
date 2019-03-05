import sys, string

def get_word_list(file_name = 'text2.txt'):
    '''Loads words from a file and cleans text of most special characters'''

    text =  open(file_name).read()
    # TODO: open with with instead of open()

    # removes punctuation from text and sets all ensures all characters are lower case
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower()
    words = (text.translate(translator)).split()

    # sorts words alphabetically
    # words = sorted(words)
    # with open(file_name,'r') as f:
    #     words = []
    #     read_words = f.readlines()
    #
    #     for line in read_words:
    #         split_line = line.strip().split(" ")
    #         for word in split_line:
    #             if(word.lower() != ""):
    #                 words.append(word.lower().strip("(),!."""))
    return words

if __name__ == '__main__':
    if len(sys.argv) == 2:
        word_list = get_word_list(sys.argv[1])
    else:
        word_list = get_word_list()

    # print()
    print(word_list)