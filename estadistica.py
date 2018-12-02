from numpy import size

from nltk.corpus import cess_esp as cess
from nltk import UnigramTagger as ut
from nltk import BigramTagger as bt
import nltk
import sys

reload(sys)
sys.setdefaultencoding('utf8')

cess_sents = cess.tagged_sents()

uni_tag = ut(cess_sents)


f = open ('texto.txt')
tagged_words = nltk.word_tokenize(f.read())
uni_tag.tag(tagged_words)

train = int(len(cess_sents)*90/100)

bi_tag = bt(cess_sents[:train], backoff=uni_tag)

bi_tag.evaluate(cess_sents[train+1:])


def word_features(word):
    return {'last_letters': word[-2:]}

labeled_names = []
taggedText=bi_tag.tag(tagged_words)
for item in taggedText:
    if item[1] is None:
        labeled_names.append({item[0],'NOMBRE'})
    elif len(item[1]) > 2:
        labeled_names.append({item[0],item[1]})

import random
#random.shuffle(labeled_names)

featuresets = [(word_features(n), tag) for (n, tag) in labeled_names]
print featuresets
train_set, test_set = featuresets[50:], featuresets[:50]
clasiffier = nltk.NaiveBayesClassifier.train(train_set)

print(clasiffier.classify(word_features('ordenador')))
print(clasiffier.classify(word_features('ejecutar')))

print(clasiffier.show_most_informative_features(5))


sys.exit()

