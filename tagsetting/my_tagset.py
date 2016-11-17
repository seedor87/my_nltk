import nltk, sys, prettytable
from nltk import word_tokenize

"""
GENERAL FORMAT

text = word_tokenize("Monkey on the car! F*** Off")
sentence = nltk.pos_tag(text)
print sentence
"""

dictionary = {
    "$": ('dollar', '$ -$ --$ A$ C$ HK$ M$ NZ$ S$ U.S.$ US$'),
    '\'\'': ('closing quotation mark', '\'\' \'\''),
    '(': ('opening parenthesis', '( [ {'),
    ')': ('closing parenthesis', ') ] }'),
    ',': ('comma', ','),
    '--': ('dash', '--'),
    '.': ('sentence terminator', '. ! ?'),
    ':': ('colon or ellipsis', ': ; ...'),
    'CC': ('conjunction, coordinating', ' & \'n and both but either et for less minus neither nor or plus so therefore times v. versus vs. whether yet'),
    'DD': ('determiner', 'all an another any both del each either every half la many much nary neither no some such that the them these this those'),
    'EE': ('existential there', 'there'),
    'FW': ('foreign word', 'gemeinschaft hund ich jeux habeas Haementeria Herr K\'ang-si vous lutihaw alai je jour objets salutaris fille quibusdam pas trop Monte terram fiche oui corporis ...'),
    'IN': ('preposition or conjunction, subordinating', 'astride among uppon whether out inside pro despite on by throughout below within for towards near behind atop around if like until below next into if beside ...'),
    'JJ': ('adjective or numeral, ordinal', 'third ill-mannered pre-war regrettable oiled calamitous first separable ectoplasmic battery-powered participatory fourth still-to-be-named multilingual multi-disciplinary ...'),
    

}


if __name__ == '__main__':



    while 1:
        table = prettytable.PrettyTable(['WORD', 'Part of Speech'])
        text = raw_input("Please enter something: ")
        if text == 'q':
            break
        text = word_tokenize(text)
        sentence = nltk.pos_tag(text)
        for tup in sentence:
            table.add_row(tup)
        print table
    print 'DONE'
    sys.exit(0)