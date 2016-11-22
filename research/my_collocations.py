import nltk
from nltk.collocations import *
from pprint import pprint

"""
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(nltk.corpus.genesis.words('english-web.txt'))
print finder.nbest(bigram_measures.pmi, 10)  # doctest: +NORMALIZE_WHITESPACE
"""

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

def get_text(file):
    import re

    """Read text from a file, normalizing whitespace and stripping HTML markup."""
    text = open(file).read()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub('\s+', ' ', text)
    return text

string = get_text('GraphDatabaseEvaluationandImplementationCon-ops.txt')
string = string.decode('utf-8').strip()
finder = BigramCollocationFinder.from_words(nltk.word_tokenize(string))
finder.apply_freq_filter(3) # Filter only those that occur three or more
print finder.nbest(bigram_measures.pmi, 10)  # doctest: +NORMALIZE_WHITESPACE

print '-'*100

string = get_text('GraphDatabaseEvaluationandImplementationCon-ops.txt')
string = string.decode('utf-8').strip()
finder = BigramCollocationFinder.from_words(nltk.pos_tag(nltk.word_tokenize(string)))
finder.apply_freq_filter(3) # Filter only those that occur three or more
pprint(finder.nbest(bigram_measures.pmi, 10))  # doctest: +NORMALIZE_WHITESPACE

print '-'*100

text = "I do not like green eggs and ham, I do not like them Sam I am!"

tokens = nltk.wordpunct_tokenize(text)
finder = BigramCollocationFinder.from_words(tokens)
scored = finder.score_ngrams(bigram_measures.raw_freq)
print sorted(bigram for bigram, score in scored)  # doctest: +NORMALIZE_WHITESPACE

finder = TrigramCollocationFinder.from_words(tokens)
scored = finder.score_ngrams(trigram_measures.raw_freq)
print sorted(bigram for bigram, score in scored)  # doctest: +NORMALIZE_WHITESPACE