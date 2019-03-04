import sys
import cleanup
import tokenize
import tweet_histogram
import sample

def sentence(histo, total, loop):
    loops = int(loop)
    sentence = []
    starter_word = " "
    for i in range(0, loops):
        weight_word = sample.weighted_random(histo, total)
        sentence.append(weight_word)
    words = starter_word.join(word for word in sentence)
    return words


if __name__ == "__main__":
    params = sys.argv[1:]
    file = params[0]
    loops = params[1]
    words = cleanup.cleanup(file)
    histo = tweet_histogram.dictogram_words(words)
    total = tweet_histogram.sum(histo)
    print(sentence(histo, total, loops))
