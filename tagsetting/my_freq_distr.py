import nltk, sys, prettytable
from pprint import pprint
from nltk import FreqDist
import nltk.book as books


# with open('/path/to/file') as FileObj:
#     for lines in FileObj:
#         print lines # or do some other thing with the line...

text = books.text6
fdist1 = FreqDist(text)
pprint(fdist1.most_common(50))

text = books.text3
fdist1 = FreqDist(text)
pprint(fdist1.most_common(50))

text = books.text7
fdist1 = FreqDist(text)
pprint(fdist1.most_common(50))