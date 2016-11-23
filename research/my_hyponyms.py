
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk.stem.wordnet import WordNetLemmatizer

# print list(swn.senti_synsets('slow')) # doctest: +NORMALIZE_WHITESPACE

print wn.synset('green.n.01').usage_domains()

print WordNetLemmatizer().lemmatize("bombast", pos="a")

# for synset in list(wn.all_synsets('a')):
#     print(synset)

# sets = wn.synsets('green')
#
# for set in sets:
#     print str(set)
#
# for set in sets:
#     print set.lemma_names()
#
# print '-'*100
# set = sets[0]
# print set.hypernyms()
#
# print set.hyponyms()
# print set.hyponyms()[0]
# print set.hyponyms()[0].root_hypernyms()
#
# print set.hyponyms()[0].root_hypernyms()[0].hypernyms()
#
# print set
# print wn.synset('dog.n.01').lowest_common_hypernyms(set)
#
# vocal = wn.lemma(set.lemmas()[0])
# print vocal.derivationally_related_forms()

#
# print wn.synset('car.n.01').lemmas()
#
# motorcar = wn.synset('car.n.01')
# print motorcar
#
# print motorcar.hyponyms()
#
# paths = motorcar.hypernym_paths()
# print paths
# print [synset.name() for synset in paths[0]]
# print [synset.name() for synset in paths[1]]