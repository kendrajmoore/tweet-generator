import sys
import re
import random

def cleanup(file):
    with open(file, 'r') as dirty_text:
        no_chapters = re.sub('[A-Z]{3,}', ' ', dirty_text.read())
        remove_periods = re.sub('(\s\.){4,}', '', no_chapters)
        remove_punctuation = re.sub(r"\W", " " , remove_periods)
    return remove_punctuation
    

if __name__ == "__main__":
    params = sys.argv[1:]
    file = params[0]
    clean_text = cleanup(file)
    print(clean_text)