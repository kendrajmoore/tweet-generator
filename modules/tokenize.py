import sys
import cleanup
#step two


def unique_words(words):
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words


if __name__ == "__main__":
    params = sys.argv[1:]
    file = params[0]
    word_list = cleanup.cleanup(file)
    # print(word_list)
    unique_word_list = unique_words(word_list)
    print(unique_word_list)
