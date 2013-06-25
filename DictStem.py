#!/usr/bin/python
import sys
import os
import nltk
from nltk import WordNetLemmatizer

#SpellChecks items in an array
def Check(mArray):

    #what am I checking?
    #Taking the 2nd item in the array since popopen puts the file path as the first item.
    item = mArray[1]
    lmtzr = WordNetLemmatizer()
    item = lmtzr.lemmatize(item)
        
    #converts to a string
    return ''.join(item)

print Check(sys.argv)    
