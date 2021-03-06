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
    'DT': ('determiner', 'all an another any both del each either every half la many much nary neither no some such that the them these this those'),
    'EX': ('existential there', 'there'),
    'FW': ('foreign word', 'gemeinschaft hund ich jeux habeas Haementeria Herr K\'ang-si vous lutihaw alai je jour objets salutaris fille quibusdam pas trop Monte terram fiche oui corporis ...'),
    'IN': ('preposition or conjunction, subordinating', 'astride among uppon whether out inside pro despite on by throughout below within for towards near behind atop around if like until below next into if beside ...'),
    'JJ': ('adjective or numeral, ordinal', 'third ill-mannered pre-war regrettable oiled calamitous first separable ectoplasmic battery-powered participatory fourth still-to-be-named multilingual multi-disciplinary ...'),
    'JJR': ('adjective, comparative', 'bleaker braver breezier briefer brighter brisker broader bumper busier calmer cheaper choosier cleaner clearer closer colder commoner costlier cozier creamier crunchier cuter ...'),
    'JJS': ('adjective, superlative', 'calmest cheapest choicest classiest cleanest clearest closest commonest corniest costliest crassest creepiest crudest cutest darkest deadliest dearest deepest densest dinkiest...'),
    'LS': ('list item marker', 'A A. B B. C C. D E F First G H I J K One SP-44001 SP-44002 SP-44005 SP-44007 Second Third Three Two * a b c d first five four one six three two'),
    'MD': ('modal auxiliary', 'can cannot could couldn\'t dare may might must need ought shall should shouldn\'t will would'),
    'NN': ('noun, common, singular or mass', 'common-carrier cabbage knuckle-duster Casino afghan shed thermostat investment slide humour falloff slick wind hyena override subhumanity machinist ...'),
    'NNP': ('noun, proper, singular', 'Motown Venneboerger Czestochwa Ranzer Conchita Trumplane Christos Oceanside Escobar Kreisler Sawyer Cougar Yvette Ervin ODI Darryl CTCA Shannon A.K.C.Meltex Liverpool...'),
    'NNPS': ('noun, proper, plural', 'Americans Americas Amharas Amityvilles Amusements Anarcho - Syndicalists Andalusians Andes Andruses Angels Animals Anthony Antilles Antiques Apache Apaches Apocrypha...'),
    'NNS': ('noun, common, plural', 'undergraduates scotches bric - a - brac products bodyguards facets coasts divestitures storehouses designs clubs fragrances averages subjectivists apprehensions muses factory - jobs...'),
    'PDT': ('pre - determiner', 'all both half many quite such sure this'),
    'POS': ('genitive marker', '\' \'s'),
    'PRP': ('pronoun, personal', 'hers herself him himself hisself it itself me myself one oneself ours ourselves ownself self she thee theirs them themselves they thou thy us'),
    'PRP$': ('pronoun, possessive', 'her his mine my our ours their thy your'),
    'RB': ('adverb', 'occasionally unabatingly maddeningly adventurously professedly stirringly prominently technologically magisterially predominately swiftly fiscally pitilessly ...'),
    'RBR': ('adverb, comparative', 'further gloomier grander graver greater grimmer harder harsher healthier heavier higher however larger later leaner lengthier less - perfectly lesser lonelier longer louder lower more...'),
    'RBS': ('adverb, superlative', 'best biggest bluntest earliest farthest first furthest hardest heartiest highest largest least less most nearest second tightest worst'),
    'RP': ('particle', 'aboard about across along apart around aside at away back before behind by crop down ever fast for forth from go high i.e.in into just later low more off on open out over per pie raising start teeth that through under unto up up-pp upon whole with you'),
    'SYM': ('symbol', '% & \' \'\' \'\'. ) ). * + ,. < = > @ A[fj] U.S U.S.S.R * ** ***'),
    'TO': ('"to" as preposition or infinitive marker', 'to'),
    'UH': ('interjection', 'Goodbye Goody Gosh Wow Jeepers Jee - sus Hubba Hey Kee - reist Oops amen huh howdy uh dammit whammo shucks heck anyways whodunnit honey golly man baby diddle hush sonuvabitch...'),
    'VB': ('verb, base form', 'ask assemble assess assign assume atone attention avoid bake balkanize bank begin behold believe bend benefit bevel beware bless boil bomb boost brace break bring broil brush build...'),
    'VBD': ('verb, past tense', 'dipped pleaded swiped regummed soaked tidied convened halted registered cushioned exacted snubbed strode aimed adopted belied figgered speculated wore appreciated contemplated...'),
    'VBG': ('verb, present participle or gerund', 'telegraphing stirring focusing angering judging stalling lactating hankerin\' alleging veering capping approaching traveling besieging encrypting interrupting erasing wincing...'),
    'VBN': ('verb, past participle', 'multihulled dilapidated aerosolized chaired languished panelized used experimented flourished imitated reunifed factored condensed sheared unsettled primed dubbed desired...'),
    'VBP': ('verb, present tense, not 3rd person singular', 'predominate wrap resort sue twist spill cure lengthen brush terminate appear tend stray glisten obtain comprise detest tease attract emphasize mold postpone sever return wag ...'),
    'VBZ': ('verb, present tense, 3rd person singular', 'bases reconstructs marks mixes displeases seals carps weaves snatches slumps stretches authorizes smolders pictures emerges stockpiles seduces fizzes uses bolsters slaps speaks pleads ...'),
    'WDT': ('WH-determiner', 'that what whatever which whichever'),
    'WP': ('WH-pronoun', 'that what whatever whatsoever which who whom whosoever'),
    'WP$': ('WH-pronoun, possessive', 'whose'),
    'WR': ('Wh-adverb', 'how however whence whenever where whereby whereever wherein whereof why'),
    '``': ('opening quotation mark', '` ``')
}


if __name__ == '__main__':

    def get_table(sentence):
        table = prettytable.PrettyTable(['WORD', 'Part of Speech', 'Description', 'Examples'])
        for tup in sentence:
            info = dictionary[tup[1]]
            table.add_row([tup[0], tup[1], info[0], info[1][:50]])
        return table

    def get_dict(sentence, filter=None):
        if filter is not None:
            _filter = filter
        else:
            _filter = set([tup[1] for tup in sentence])
        ret = dict([(key, []) for key in _filter])
        [ret[tup[1]].append(tup[0]) if tup[1] in _filter else None for tup in sentence]
        return ret

    while 1:
        text = raw_input("Please enter something: ")
        if text == 'q':
            break
        text = word_tokenize(text)
        sentence = nltk.pos_tag(text)
        # print get_table(sentence)
        print get_dict(sentence)
    print 'DONE'
    sys.exit(0)

"""
Test-set:

test
testing
tested
testers
(phrase test)
"""