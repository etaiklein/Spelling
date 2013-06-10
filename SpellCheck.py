import enchant
import string
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

#SpellChecks a file and uses stemming to filter out repeated words
def Spell_Stem(dictionary, mfile, stemlength=5):
    d = dictionary
    f = mfile
    print f
    mymap = {}
    
    #spellchecks and takes the first suggestion. 
    #TODO - frequency based spellcheck would be more accurate
    for item in f:
        if (d.check(item) == False):
            print "item " + item + " was misspelled. \"" + d.suggest(item)[0] + "\" suggested"
            item = d.suggest(item)[0]

        #stems (lemmatizes) the words        
        lmtzr = WordNetLemmatizer()
        stem = lmtzr.lemmatize(item)
        
        #and counts them using the map
        if mymap.has_key(stem):
            mymap[stem] += 1
        else:
            mymap[stem] = 0
    
    print mymap.items()

#--------------------Helper functions-------------------------#
def read_file(filename):
    text = open(filename).read().lower()
    text = filter(lambda x:x in string.lowercase or x in string.whitespace, text).split()
    return text
def stem_file(text, stemlength):
        stemlength = int(stemlength)
        stemmed = map(lambda word: word[:min(len(word), stemlength)], text)
        return stemmed

##-----------------------------unused functions-------------#
##Basic Hello world spell checker
#def enchant_test(dictionary):
#    print d.check("Hello World")
#    print d.suggest("Helo")
#    
##SpellChecks a file and uses stemming to filter out repeated words
#def trie_test(dictionary, mfile, stemlength=5):
#    d = dictionary
#    f = mfile
#    #A Trie is a recursive data structure storing words by their prefix.
#    #I don't have a reason for choosing this instead of a different data structure other than to try it out.
#    e = enchant.pypwl.Trie()
#    print f
#    mymap = {}
#    
#    #spellchecks and takes the first suggestion. 
#    #TODO - frequency based spellcheck would be more accurate
#    for item in f:
#        if (d.check(item) == False):
#            print "item " + item + " was misspelled. " + d.suggest(item)[0] + "suggested"
#            item = d.suggest(item)[0]
#        print "item: " + item 
#        
#        #The map checks if the stems are repeats
#        #stem = item[:min(len(item), stemlength)]
#        lmtzr = WordNetLemmatizer()
#        stem = lmtzr.lemmatize(item)
#        if mymap.has_key(stem):
#            print "repeat"
#        else:
#            mymap[stem] = 1
#            e.insert(item)
#            print stem
#            
#    for key in e:
#        print key
#    
#    #testing the search function
#    print e.search("particular")

#driver

d = enchant.Dict("en_US")
f =  read_file("English-Latin-misspell")
Spell_Stem(d, f)
