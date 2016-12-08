from nltk.corpus import wordnet as wn
from collections import defaultdict
from pprint import pprint
from pprint import pprint

def dictify(d, steps=3):
    if steps < 1:
        for i in xrange(10):
            d[i] = i
    else:
        for i in xrange(10):
            d[i] = {}
            dictify(d[i], steps-1)

def tup_as_key():
    list = {}
    list[(1, "test")] = "accepted"
    print list

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

def key_wrap(syn_set):
    _syn_set = str(syn_set)
    index_first_period = _syn_set.find('.')
    word = _syn_set[8:index_first_period]
    return word

# syn_sets = wn.synsets(raw_input('Enter the word here >>> '))
syn_sets = wn.synsets('test')
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