from functools import wraps
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk.stem.wordnet import WordNetLemmatizer
from pprint import pprint

def mult_decorator(func):

    @wraps(func)
    def wrapper(word, pos=None):
        if pos is None:
            ret = {}
            poses = [wn.NOUN, wn.ADJ, wn.VERB, wn.ADV]
            for _pos in poses:
                ret[_pos] = func(word, pos=_pos)
            return ret
        return func(word, pos=pos)
    return wrapper

@mult_decorator
def gen_synsets(word, pos=None):
    if pos is None:
        return wn.synsets(word)
    return wn.synsets(word, pos=pos)

@mult_decorator
def gen_lemmas(synset, pos=None):
    if pos is None:
        return synset.lemmas()
    return synset.lemmas()

def gen_hypernyms(word, pos=None):

    if pos is None:
        ret = {}
        poses = [wn.NOUN, wn.ADJ, wn.VERB, wn.ADV]
        for _pos in poses:
            sets = [set.lemmas() for set in wn.synsets(word, pos=_pos)]
            ret[_pos] = sets
        return ret
    else:
        sets = [set.lemmas() for set in wn.synsets(word, pos=pos)]
        return sets

def gen_lemmas(word, pos=None):

    if pos is None:
        ret = {}
        poses = [wn.NOUN, wn.ADJ, wn.VERB, wn.ADV]
        for _pos in poses:
            sets = [set.lemmas() for set in wn.synsets(word, pos=_pos)]
            ret[_pos] = sets
        return ret
    else:
        sets = [set.lemmas() for set in wn.synsets(word, pos=pos)]
        return sets

def gen_definitions(word, pos=None):

    if pos is None:
        ret = {}
        poses = [wn.NOUN, wn.ADJ, wn.VERB, wn.ADV]
        for _pos in poses:
            sets = [str(set) + ' ' + set.definition() for set in wn.synsets(word, pos=_pos)]
            ret[_pos] = sets
        return ret
    else:
        sets = [str(set) + ' ' + set.definition() for set in wn.synsets(word, pos=pos)]
        return sets


if __name__ == '__main__':

    total = {}
    test_word = 'train'
    poses = [wn.NOUN, wn.ADJ, wn.VERB, wn.ADV]
    for pos in poses:
        total[str(pos)] = {}
        sets = wn.synsets(test_word)
        for set in wn.synsets(test_word):
            total[str(pos)][str(set)] = {}
            for lemma in set.lemmas():
                total[str(pos)][str(set)][str(lemma)] = {}
                for string in lemma.frame_strings():
                    total[str(pos)][str(set)][str(lemma)][str(string)] = string


    import json
    with open('data.json', 'w') as fp:
        json.dump(total, fp, sort_keys=True, indent=4)