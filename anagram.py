import sys
import random

def list_words(file):
    f = open(file, "r")
    list = f.read().split()
    f.close()
    return list

