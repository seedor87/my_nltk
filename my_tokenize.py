from __future__ import division
import nltk, re
from pprint import pprint
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
pprint(nltk.pos_tag(text))


text = word_tokenize("They refuse to permit us to obtain the refuse permit")
print text
print nltk.pos_tag(text)

print "-" * 100

text = word_tokenize("To win is to be victorious")
sentence = nltk.pos_tag(text)
print sentence

tagged_token = nltk.tag.str2tuple('win/NN')
print tagged_token

text = word_tokenize("There is a win on the car!")
sentence = nltk.pos_tag(text)
print sentence

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result
# result.draw()

nltk.help.upenn_tagset('.*')