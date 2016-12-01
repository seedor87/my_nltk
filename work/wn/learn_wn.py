
"""
hypernym - a word with a broad meaning that more specific words fall under; a superordinate. For example, color is a hypernym of red.

hyponym - a word of more specific meaning than a general or superordinate term applicable to it. For example, spoon is a hyponym of cutlery.

lemma - a heading indicating the subject or argument of a literary composition, an annotation, or a dictionary entry.
"""
from pprint import pprint
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn

print '-' *25, 'demo synonyms', '-' *25
print 'slow:', list(swn.senti_synsets('slow'))

print '-' *25, 'demo print all adjectives', '-' *25
for synset in list(wn.all_synsets('a')):
    print(synset)

print '-' *25, 'demo lemmas', '-' *25
print 'word : green'
sets = wn.synsets('green')

for set in sets:
    print str(set)

for set in sets:
    print set.lemma_names()

print '-' *25, 'demo hypernyms', '-' *25
print 'word: green'

set = sets[0]
print 'set[0]:', set

print 'set.hypernyms:', set.hypernyms()

print 'set.hyponyms:', set.hyponyms()

print 'set.hyponyms[0]', set.hyponyms()[0]

print 'set.hyponyms[0].root_hypernyms:', set.hyponyms()[0].root_hypernyms()

print '-' *25, 'demo lowest_common_hypernyms', '-' *25
print 'word2: dog'
print 'word2.lowest_common_hypernym(set):', wn.synset('dog.n.01').lowest_common_hypernyms(set)

# print '-' *25, 'derivationally related terms', '-' *25
# vocal = wn.lemma(set.lemma_names()[0])
# print vocal.derivationally_related_forms()

print '-' *25, 'demo path tracing', '-' *25
print wn.synset('car.n.01').lemmas()

motorcar = wn.synset('car.n.01')
print motorcar

print motorcar.hyponyms()
print
print
paths = motorcar.hypernym_paths()
print paths
print
print
print "path:", paths[0][:50]
pprint([synset.name() for synset in paths[0]])