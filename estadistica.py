

from nltk.corpus import cess_esp as cess
from nltk import UnigramTagger as ut
from nltk import BigramTagger as bt
import nltk
import sys


def word_features(word):
    return {'last_letters': word[-4:]}

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


taggedText=bi_tag.tag(tagged_words)

labeled_names = ([word, tag] for word, tag in taggedText)

featuresets = [(word_features(n), tag) for (n, tag) in labeled_names]

for item in featuresets:
    print (item)
train_set, test_set = featuresets[250:], featuresets[:250]
clasiffier = nltk.NaiveBayesClassifier.train(train_set)


print(clasiffier.show_most_informative_features(10))


sys.exit()

