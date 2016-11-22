
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn

print list(swn.senti_synsets('slow')) # doctest: +NORMALIZE_WHITESPACE

print wn.synsets('motorcar')

print wn.synset('car.n.01').lemma_names()

print wn.synset('car.n.01').lemmas()

motorcar = wn.synset('car.n.01')
print motorcar

print motorcar.hyponyms()

paths = motorcar.hypernym_paths()
print paths
print [synset.name() for synset in paths[0]]
print [synset.name() for synset in paths[1]]