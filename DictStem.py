#!/usr/bin/python
import sys
import os
import string

#put the path of your enchant library here
sys.path.append("/Library/Python/2.7/site-packages/pyenchant-1.6.5-py2.5-macosx-10.4-universal")
import nltk
from nltk import WordNetLemmatizer
import enchant

#SpellChecks items in an array
def Check(mArray):

    #what am I checking?
    print "\nmy array= ", mArray

    mylist = []

    d = enchant.Dict("en_US")
    
    f = mArray

    #preprocess is the word, post is a boolean-
    i = 0
    while i < len(f):
        print "\npreprocess= " + f[i]
        
        if (d.check(f[i]) != False):
            lmtzr = WordNetLemmatizer()
            #comma for later delimatizing
            f[i] = lmtzr.lemmatize(f[i].lower()) + ","
        #am I a word?
        print "postprocess= ", f[i]
        i += 1
        
    #converts to a string
    return ''.join(f)

print Check(sys.argv[1:])    
