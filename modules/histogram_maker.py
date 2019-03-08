import sys

def get_source_text(file_name):
    punctuations = """!@#$%^&*()_-+=[]{}\|;:,./<>?`~"""
    source = open(file_name, 'r').read().replace("\n", "").split()
    for word in source:
        for character in word:
            if character in punctuations:
                word_index = source.index(word)
                source.pop(word_index)
                new_word = word.replace(character, "")
                word = new_word
                continue
            else:
                pass
    return source

def histogram(source_text):
    initial_histogram = []
    for word in source_text:
        count_and_word = []
        word_count = source_text.count(word)
        count_and_word.append(word_count)
        count_and_word.append(word)
        initial_histogram.append(count_and_word)
    histogram = []
    for list in initial_histogram:
        if list not in histogram:
            histogram.append(list)
        else:
            pass
    return histogram

def unique_words(histogram):
    unique_words_count = 0
    for gram in histogram:
        unique_words_count += 1
    return unique_words_count


def frequency(word, histogram):
    frequency_counter = 0
    for gram in histogram:
        if gram[1] == word:
            frequency_counter += gram[0]
        else:
            pass
    return frequency_counter

if __name__ in '__main__':
    source_text = get_source_text("twilight.txt")
    histogram = histogram(source_text)
    print(histogram)
    unique_words = unique_words(histogram)
    frequency = frequency("light", histogram)