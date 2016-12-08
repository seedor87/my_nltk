from nltk.corpus import wordnet as wn
from collections import defaultdict
from pprint import pprint

def decypher(pos, word):
    if pos is 'NN' or pos is 'NNS' or pos is 'NNP' or pos is 'NNPS':
        return word, 'n'
    elif pos is 'VB' or pos is 'VBD' or pos is 'VBG' or pos is'VBN' or pos is 'VBP' or pos is'VBZ':
        return word, 'v'
    elif pos is 'JJ' or pos is 'JJS' or pos is 'JJR':
        return word, 'a'
    else:
        raise Exception("Invalid pos")

def synset_method_values(synset):
    """
    For a given synset, get all the (method_name, value) pairs
    for that synset. Returns the list of such pairs.
    """
    name_value_pairs = []
    # All the available synset methods:
    method_names = ['hypernyms', 'instance_hypernyms', 'hyponyms', 'instance_hyponyms',
                    'member_holonyms', 'substance_holonyms', 'part_holonyms',
                    'member_meronyms', 'substance_meronyms', 'part_meronyms',
                    'attributes', 'entailments', 'causes', 'also_sees', 'verb_groups',
                    'similar_tos']
    for method_name in method_names:
        # Get the method's value for this synset based on its string name.
        method = getattr(synset, method_name)
        vals = method()
        if not vals or vals is [] or vals is None:
            pass
        else:
            name_value_pairs.append((method_name, vals))
    return name_value_pairs

def gen_closure(syn_set, steps):
    ret = {}
    n = 1
    while n <= steps:
        for method, sets in synset_method_values(syn_set):
            for set in sets:
                ret[method] = (list(set.closure(method, depth=n)))
        yield ret
        n += 1

def dictify_on_node(dict, syn_set, path, steps=2):
    for method, sets in synset_method_values(syn_set):
        for set in sets:
            _path = list(path)
            _path.append((syn_set, method))
            key = key_wrap(set)
            if steps < 1:
                dict[key] = _path
            else:
                dict[key] = {}
                dictify_on_node(dict, set, _path, steps - 1)

def dictify_on_method(dict, syn_set, steps=3):
    for syn in syn_set:
        for method, sets in synset_method_values(syn):
            if steps < 1:
                dict[method] = (method, syn)
            else:
                dict[method] = {}
                dictify_on_method(dict[method], sets, steps - 1)

def key_wrap(syn_set):
    _syn_set = str(syn_set)
    index_first_period = _syn_set.find('.')
    word = _syn_set[8:index_first_period]
    pos = _syn_set[index_first_period + 1]
    num = _syn_set[-4:-2]
    return word, pos, num

def main(key='method'):

    if key is 'method':
        while 1:
            total = {}
            dictify_on_method(total, wn.synsets(raw_input('Enter the word here >>> ')), steps=2)
            pprint(total)
    else:
        while 1:
            total = {}
            for syn_set in wn.synsets(raw_input('Enter the word here >>> ')):
                dictify_on_node(total, syn_set, [], steps=2)
            pprint(total)

def test():
    print "testing"

    def key_wrap(syn_set):
        _syn_set = str(syn_set)
        index_first_period = _syn_set.find('.')
        word = _syn_set[8:index_first_period]
        return word

    syn_sets = wn.synsets(raw_input('Enter the word here >>> '))
    total = {}
    for syn_set in syn_sets:
        key = key_wrap(syn_set)
        total[key] = {}
        for method, sets in synset_method_values(syn_set):
            total[key][method] = {}
            for set in sets:
                _key = key_wrap(set)
                total[key][method][_key] = {}
                for _method, _sets in synset_method_values(set):
                    total[key][method][_key][_method] = {}
                    for _set in _sets:
                        __key = key_wrap(_set)
                        total[key][method][_key][_method][__key] = {}
                        for __method, __sets in synset_method_values(_set):
                            total[key][method][_key][_method][__key][__method] = [key_wrap(__set) for __set in __sets]

    pprint(total)
    print total['quiz']['hypernyms']['examine']

    # total = {}
    # for syn_set in wn.synsets(raw_input('Enter the word here >>> ')):
    #     dictify_on_node(total, syn_set, [], steps=2)
    # pprint(total)
    #
    # total = {}
    # dictify_on_method(total, wn.synsets(raw_input('Enter the word here >>> ')), steps=2)
    # pprint(total)
    #
    # print total['hypernyms']['hyponyms']

if __name__ == '__main__':
    # main(key='node')
    test()

