from __future__ import division, print_function

class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type"""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words"""
        super(Listogram, self).__init__() # initialize as a new list
        # add properties to track useful word counts for this histogram
        self.types = 0 # count of distinct word types in this histogram
        self.tokens = 0 # total count of all word tokens in this histogram
        # count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of a given word by given count amount"""
        if word in self:
            index = self._index(word)
            self[index] = (self[index][0], self[index][1] + count)
        else:
            self.append((word, count))
            self.types += 1
        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found"""
        index = self._index(word)
        return 0 if index is None else self[index][1]

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram"""
        return word in dict(self)

    def _index(self, target):
        """Return the index of entry containing given target word if found
        in this histogram, or None if target word is not found"""
        words, counts = zip(*self)
        return None if target not in self else words.index(target)

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:] # exclude scrupt name in first argument
    if len(arguments) >= 1:
        # test histogram on given arguments
        # type in the words for the histogram
        print_histogram(arguments)
    else:
        # test histogram on letter in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # test histogram on words in a class book ^__^
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                            ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())

if __name__ == '__main__':
    main()