""" code and app structure based on Edwin C. tweet gen """

import string

def clean(words):
    """Attempts to remove puncuantion and abbreviations but it broken """
    translation_table = str.maketrans(
        '', '', '''!"#$%&()*+,./:;<=>?@[\]^_`{|}~`1234567890''')
    words[:] = [i.replace(' ', '') for e in words for i in e.split('--')]
    alphabet = [i + '.' for i in string.ascii_uppercase]
    single_letter_words = ['a', 'b', 'i']
    abbreviations3 = ['st.', 'dr.', 'mr.']
    abbreviations4 = ['mrs.', 'sq.,', 'esq.']
    words[:] = [i for i in words if i[-2:] not in alphabet and
                i[-3:].lower() not in abbreviations3 and
                i[-4:].lower() not in abbreviations4 and
                not (len(i) == 1 and i.lower() not in
                    single_letter_words)]

    words[:] = [i.translate(translation_table).lower().lstrip(
        "'").rstrip("'") for i in words]
    
    return words


if __name__ == '__main__':
    import sys
    from tokenize import get_words
    words = get_words(sys.argv[1])
    cleaned_words = clean(words)

    # print cleaned up word list
    for word in cleaned_words:
        print(word)