import random
import sys 
import cleanup
import tokenize
import tweet_histogram
#four


def sum_value(hist):
    dict_total = int((sum(hist.values())))
    return dict_total

# takes a histogram and returns a weighted probabibility
def weighted_random(hist, total):
    destination = random.randint(0, total)
    for word in hist:
        destination = destination - hist[word]
        if destination <= 0:
            return word

if __name__ == "__main__":
    params = sys.argv[1:]
    file = params[0]
    words = cleanup.cleanup(file)
    histo = tweet_histogram.dictogram_words(words)
    # print(histo)
    value = sum_value(histo)
    # print(value)
    weight = weighted_random(histo, value)
    print(weight)

   