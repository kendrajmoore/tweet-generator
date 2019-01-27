import random
import sys


def dict():
    """ get words from words file """
    f = open("/usr/shar/dict/words", "r")
    words = f.read().split()
    f.close()
    return words

def words()