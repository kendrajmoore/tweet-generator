def words_list(file):
    "Open the file and make the words into a list to be used by markov"    
    if 'modules' in sys.path[0]:
        path = 'corpuses/'
    else:
        path = 'modules/corpuses/'
    with open(path + file) as file:
        words = file.read().split()
    return words


if __name__ == "__main__":
    import sys
    words = words_list(sys.argv[1])
    for word in words:
        print(word)

    
