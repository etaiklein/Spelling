#!/usr/bin/python
import sys
import nltk
from nltk.corpus import wordnet as wn
#SpellChecks a single item
def Checkitem(item):
    item = item[1]

    #checks if it is a word
    if not wn.synsets(item):
        return "False"
    else:
        return "True"

print Checkitem(sys.argv)    
