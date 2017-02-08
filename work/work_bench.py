from __future__ import division
import nltk, sys
from nltk import FreqDist
from nltk.corpus import inaugural

def get_text(file):
    import re

    """Read text from a file, normalizing whitespace and stripping HTML markup."""
    text = open(file).read()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub('\s+', ' ', text)
    return text

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                  if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

def find_similar(text, word):
    return text.similar(word)

def produce_tagged(body):
    tokenized = nltk.word_tokenize(body)
    tagged = nltk.pos_tag(tokenized)
    return tagged

def generate_frequency_by_pos(tagged, pos='NN'):
    tagdict = findtags(pos, tagged)
    for tag in sorted(tagdict):
        yield (tag, tagdict[tag])

def tag_insight(tagged, freq_thresh=2):
    data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in tagged)
    for word in sorted(data.conditions()):
        if len(data[word]) > freq_thresh:
            tags = [tag for (tag, _) in data[word].most_common(20)]
            print(word, ' '.join(tags))

if __name__ == '__main__':

    body = get_text('GraphDatabaseEvaluationandImplementationCon-ops.txt')
    body = body.decode('utf-8').strip()

    tokens = nltk.word_tokenize(body)
    text = nltk.Text(word.lower() for word in tokens)

    print 'demo find similar'
    print find_similar(text, 'word')
    print '\n'
    print '-' * 100

    print 'demo produce tagged'
    tagged = produce_tagged(body)
    print tagged
    print '\n'
    print '-' * 100

    print 'demo generator topics'
    gen = generate_frequency_by_pos(tagged, pos='NN')
    for elem in gen:
        print elem
    print '\n'
    print '-' * 100

    print 'demo tag insight'
    tag_insight(tagged)


