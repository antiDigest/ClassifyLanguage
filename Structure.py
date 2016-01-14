import nltk
import json
from nltk.data import load



def POS_tag(text):
	tokens = nltk.word_tokenize(text)

	return nltk.pos_tag(tokens)
