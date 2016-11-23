
from nltk.parse import load_parser
from nltk.sem.drt import DrtParser
parser = load_parser('grammars/book_grammars/drt.fcfg', trace=0, logic_parser=DrtParser())
for tree in parser.parse('a dog barks'.split()):
    print(tree.label()['SEM'].simplify())

for tree in parser.parse('Monkey on the car, fuck off!'.split()):
    print(tree.label()['SEM'].simplify())

