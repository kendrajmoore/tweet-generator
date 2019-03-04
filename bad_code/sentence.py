import sys
import cleanup
import tokenize
import tweet_histogram
import sample

def sentence(hist, total, loop):
    loops = int(loop)
    sentences = []
    word_string = ' '
    for i in range(0, loops):
        weighted_word = sample.weighted_random(hist, total)
        sentences.append(weighted_word)
    word_string = word_string.join(word for word in sentences)
    return word_string

if __name__ == "__main__":
    params = sys.argv[1:]
    file = params[0]
    loops = int(params[1])
    words = cleanup.cleanup(file)
    histo = tweet_histogram.dictogram_words(words)
    value = tweet_histogram.sum(histo)
    