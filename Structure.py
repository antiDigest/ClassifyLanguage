import nltk
import json
from nltk.data import load
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# tagdict = load('help/tagsets/claws5_tagset.pickle')
# print json.dumps(tagdict)

data = open('tags.txt')
k = json.load(data)

tagdict = dict(k)

# print dict(k).keys()

def POS_tag(text):
	tokens = nltk.word_tokenize(text)

	return nltk.pos_tag(tokens)
