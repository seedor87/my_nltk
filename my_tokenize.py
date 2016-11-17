from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
from nltk.corpus import nps_chat
import urllib

"""
url = "http://www.gutenberg.org/files/2554/2554.txt"
response = urllib.urlopen(url)
raw = response.read().decode('utf8')

tokens = word_tokenize(raw)
print tokens[:10]

text = nltk.Text(tokens)
text.concordance('hold')

chat = nltk.Text(nps_chat.words())
chat.findall(r"<l.*>{3,}")
"""

text = word_tokenize("And now for something completely different")
print nltk.pos_tag(text)

text = word_tokenize("They refuse to permit us to obtain the refuse permit")
print text
print nltk.pos_tag(text)

tagged_token = nltk.tag.str2tuple('fly/NN')
tagged_token