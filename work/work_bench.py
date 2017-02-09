# -*- coding: utf-8 -*-

from __future__ import division
import nltk, sys, validators, os
from pprint import pprint

def process_input(input):

    def process_string(string):
        text = string.decode('utf-8').strip()
        return text

    def process_url(url):
        import urllib
        from bs4 import BeautifulSoup
        html = urllib.urlopen(url).read().decode('utf8')
        text = BeautifulSoup(html, "lxml")
        text = text.find("div", {"class" : "article-text"})
        text = text.get_text()
        return text

    def process_file(file):
        text = get_text(file)
        text = text.decode('utf-8').strip()
        return text

    def get_text(file):
        import re

        """Read text from a file, normalizing whitespace and stripping HTML markup."""
        text = open(file).read()
        text = re.sub(r'<.*?>', ' ', text)
        text = re.sub('\s+', ' ', text)
        return text

    if validators.url(input):
        return process_url(input)
    elif os.path.exists(input):
        return process_file(input)
    else:
        return process_string(input)

def findtags(tag_prefix, tagged_text, n):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(n)) for tag in cfd.conditions())

def generate_frequency_by_pos(tagged, pos=('NN'), n=15):
    for _pos in pos:
        tagdict = findtags(_pos, tagged, n=n)
        for tag in sorted(tagdict):
            yield (tag, tagdict[tag])

def tag_insight(tagged, freq_thresh=1):
    data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in tagged)
    for word in sorted(data.conditions()):
        if len(data[word]) > freq_thresh:
            tags = [tag for (tag, _) in data[word].most_common(20)]
            print(word, ' '.join(tags))

def back_off_tagger(tagged):
    train_sents = tagged[:100]
    test_sents = tagged[100:]
    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(train_sents, backoff=t0)
    t2 = nltk.BigramTagger(train_sents, backoff=t1)
    print t2.evaluate(test_sents)

def debug():
    body = get_text(
        'C:\Users\Bob S\PycharmProjects\my_nltk\work\GraphDatabaseEvaluationandImplementationCon-ops.docx.txt')
    body = body.decode('utf-8').strip()

    tokens = nltk.word_tokenize(body)
    print tokens
    # text = nltk.Text(word.lower() for word in tokens)
    text = nltk.Text(word for word in tokens)

    print 'demo text / find similar'
    print text
    # print find_similar(tokens, 'word')
    print '\n'
    print '-' * 100

    print 'demo produce tagged'
    tagged = produce_tagged(tokens)
    print tagged
    print '\n'
    print '-' * 100

    print 'demo generator frequency'
    gen = generate_frequency_by_pos(tagged, pos='NN')
    for elem in gen:
        print elem
    print '\n'
    print '-' * 100

    print 'demo tag insight'
    tag_insight(tagged)
    print '\n'
    print '-' * 100

def main():
    """
    General flow
        i.      process input as file, url or raw text into body
        ii.     get tokens of body into tokens
        iii.    get part of speech tags into tagged
        iv.     developed strongest accuracy for classifier of tags
        iv.     generate the top strongest words for topics
    """

    # body = process_input('C:\Users\Bob S\PycharmProjects\my_nltk\work\GraphDatabaseEvaluationandImplementationCon-ops.docx.txt')
    body = process_input('http://www.foxnews.com/politics/2017/02/08/white-house-fires-back-at-immigration-order-critics-with-list-terror-arrests.html')

    tokenized = nltk.word_tokenize(body)

    # normalize text here
    text = nltk.Text(tokenized)
    # print text.similar('News')
    # print text.common_contexts(words=['News'])
    # print text.concordance('News')

    tagged = nltk.pos_tag(tokenized)
    """TODO Improve tagging methods for superior analyzation of hot words"""

    # print '-' * 100
    # tag_insight(tagged)
    # print '-' * 100

    gen = generate_frequency_by_pos(tagged=tagged, n=10, pos=('NN', 'JJ', 'VB'))

    dict = {}
    for elem in gen:
        dict[elem[0]] = elem[1]
    pprint(dict)

if __name__ == '__main__':
    main()
    sys.exit(0)
