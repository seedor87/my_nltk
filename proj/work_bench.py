from nltk.corpus import wordnet as wn
from collections import defaultdict
from pprint import pprint

def decypher(synset):
    word = synset[8:synset.find('.')]
    pos = synset[synset.find('.') + 1]
    num = synset[-4:-2]
    print word, pos, num

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

def main():
    while 1:
        total = {}
        for syn_set in wn.synsets(raw_input('Enter the word here >>> ')):
            key = str(syn_set)[8:str(syn_set).find('.')]    # grab name of the input word's synset
            total[key] = {}
            for method0, set0 in synset_method_values(syn_set):
                total[key][method0] = {}
                for a in set0:
                    for method1, set1 in synset_method_values(a):
                        total[key][method0][method1] = {}
                        for b in set1:
                            for method2, set2 in synset_method_values(b):
                                total[key][method0][method1][method2] = set2
        return total

def test():
    print decypher(synset='Synset(\'assume.v.05\')')
    pass

if __name__ == '__main__':
    ret = main()
    print ret.keys()
    for key in ret.keys():
        print '\t', ret[key]