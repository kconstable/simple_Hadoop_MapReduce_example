#!/usr/bin/env python
import sys
import re
#from sklearn.feature_extraction import stop_words
#import nltk
#from nltk.corpus import stopwords
import spacy
from spacy.lang.en.stop_words import STOP_WORDS


# get sklearn, nltk and spacy stopwords & combine them in one list
# covert to dictionary and back to list to remove any duplicates
stops = set(STOP_WORDS)
#stops = set(stop_words.ENGLISH_STOP_WORDS)
#stops_nltk = list(stopwords.words('english'))
#stops = stops_nltk + stops_sklearn + stops_spacy

#remove duplicates, convert back to a set
#stops = set(list( dict.fromkeys(stops)))
#stops = set(["the","are","there","their","a","i","and"])

# get all lines from stdin
for line in sys.stdin:

    # remove punctuation using regular expressions
    line = re.sub(r'[^\w\s]','',line)

    # remove leading and trailing whitespace, convert to lowercase
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stops:
            # print("{},{}".format(word,"1"))
             print '%s\t%s' % (word, "1")
