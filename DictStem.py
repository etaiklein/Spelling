#!/usr/bin/python
import sys
import os

#put the path of your nltk file here
#sys.append()

import nltk
from nltk import WordNetLemmatizer


#gets the part of speech of the word
def get_wordnet_pos(treebank_tag):

  if treebank_tag.startswith('J')
    return wordnet.ADJ
  elif treebank_tag.startswith('V'):
    return wordnet.VERB
  elif treebank_tag.startswith('N'):
    return wordnet.NOUN
  elif treebank_tag.startswith('R'):
    return wordnet.ADV
  else:
    return ''

#SpellChecks items in an array
def Check(mArray):

  #what am I checking?
  #Taking the 2nd item in the array since popopen puts the file path as the first item.
  item = mArray[1]
  lmtzr = WordNetLemmatizer()
  item = lmtzr.lemmatize(item, get_wordnet_pos(item))
    
  #converts to a string
  return ''.join(item)

print Check(sys.argv)    
