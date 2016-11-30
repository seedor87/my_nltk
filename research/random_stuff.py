from __future__ import division
import nltk, sys
from nltk import FreqDist
from nltk.corpus import inaugural

"""
NEEDED FOR THE INSTALLATION OF NLTK

>>> nltk.download()
"""

def lexical_diversity(text):
    word_count = len(text)
    vocab_size = len(set(text))
    diversity_score = vocab_size / word_count
    return diversity_score

def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

def target_puzzle_solver(puzzle_letters, obligatory):
    wordlist = nltk.corpus.words.words()
    return [w for w in wordlist if len(w) >= 6 and obligatory in w and nltk.FreqDist(w) <= puzzle_letters]

def percentage(count, total):
    return 100 * (count / total)


sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""

def page1():
    tokens = nltk.word_tokenize(sentence)
    print tokens

    tagged = nltk.pos_tag(tokens)
    print tagged[0:6]

def ex1():
    sent1 = ['Call', 'me', 'Ishmael', '.']
    return lexical_diversity(sent1)

def ex2():
    fdist1 = FreqDist(books.text1)
    return fdist1.most_common(50)
#     return fdist1.max()

def ex3():
    return books.text6.collocations()

def ex4():
    cfd = nltk.ConditionalFreqDist(
          (target, fileid[:4])
          for fileid in inaugural.fileids()
          for w in inaugural.words(fileid)
          for target in ['america', 'citizen']
          if w.lower().startswith(target))
    cfd.plot()

def ex5():

    from nltk.corpus import PlaintextCorpusReader
    corpus_root = '/usr/share/dict'
    wordlists = PlaintextCorpusReader(corpus_root, '.*')
    return wordlists.words('connectives')

def ex6():
    def generate_model(cfdist, word, num=15):
        for i in range(num):
            print word
            word = cfdist[word].max()

    text = nltk.corpus.genesis.words('english-kjv.txt')
    bigrams = nltk.bigrams(text)
    cfd = nltk.ConditionalFreqDist(bigrams)
    generate_model(cfd, 'living')

def ex7():
    from nltk.corpus import stopwords
    print stopwords.words('english')

def name_freq_distr():
    names = nltk.corpus.names
    male_names = names.words('male.txt')
    female_names = names.words('female.txt')
    cfd = nltk.ConditionalFreqDist(
              (fileid, name[-1])
              for fileid in names.fileids()
              for name in names.words(fileid))
    cfd.plot()

def first_last_sound_grouping():
    entries = nltk.corpus.cmudict.entries()
    p3 = [(pron[0]+'-'+pron[2], word)
        for (word, pron) in entries
        if pron[0] == 'P' and len(pron) == 3]
    cfd = nltk.ConditionalFreqDist(p3)
    for template in sorted(cfd.conditions()):
        if len(cfd[template]) > 10:
            words = sorted(cfd[template])
            wordstring = ' '.join(words)
            print(template, wordstring[:70] + "...")

def translate(frm, to, word):
    from nltk.corpus import swadesh
    frm2to = swadesh.entries([frm, to])    # from -> to
    translate= dict(frm2to)
    return translate[word]

def demo_regex():
    import re
    wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

    print [w for w in wordlist if re.search('ed$', w)]
    print [w for w in wordlist if re.search('ed$', w)]
    print [w for w in wordlist if re.search('^..j..t..$', w)]

    print [w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)] # t9 checking problem

    wsj = sorted(set(nltk.corpus.treebank.words()))
    print [w for w in wsj if re.search('^[A-Z]+\$$', w)] # use the ignore char, \, to scan and return only that which contains a certain character

def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


# print target_puzzle_solver(puzzle_letters= nltk.FreqDist('egivrvonl'), obligatory = 'r')

# name_freq_distr()

# first_last_sound_grouping()

# print translate('en', 'fr', 'dog')

# demo_regex()

print stem('expectently')

sys.exit(0)