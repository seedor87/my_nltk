from __future__ import print_function
import nltk

nltk.download()

tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
print(tokenizer.tokenize('Hello.  This is a test.  It works!'))

s = nltk.data.load('work/GraphDatabaseEvaluationandImplementationCon-ops.txt', format='raw')[:60]
print(s.decode())

s = nltk.data.load('work/GraphDatabaseEvaluationandImplementationCon-ops.txt', format='text')[:60]
print(s)