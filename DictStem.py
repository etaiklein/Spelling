#!/usr/bin/python
import sys
import os

#put the path of your enchant library here
import nltk
from nltk import WordNetLemmatizer

#SpellChecks items in an array
def Check(mArray):

    #what am I checking?
    item = mArray[1]
    lmtzr = WordNetLemmatizer()
    item = lmtzr.lemmatize(item)
        
    #converts to a string
    return ''.join(item)

print Check(sys.argv)    
