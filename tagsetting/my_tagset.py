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