import sys 

def words_list(file):
    "Open the file and make the words into a list to be used by markov"
    # you need to be on the right path    
    if 'modules' in sys.path[0]:
        path = 'corpuses/'
    else:
        path = 'modules/corpuses/'
    # use with so do not have to close
    with open(path + file) as file:
        words = file.read().split()
    return words


if __name__ == "__main__":
    words = words_list(sys.argv[1])
    for word in words:
        print(word)

    
