from nltk import tag
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# def BrillTag(filename):

def posgrams(filename):
	with open(filename,'r') as f:
		data = f.read()

	data = data.decode('utf-8')
	bigram_vectorizer = CountVectorizer(ngram_range=(2,3),token_pattern=r'\b\w+\b', min_df=1)
	analyze = bigram_vectorizer.build_analyzer()

	output = analyze(data)

	training_data = nltk.pos_tag(output)

	# print training_data

	count_vect = CountVectorizer(preprocessor=lambda x:x,tokenizer=lambda x:x)
	
	X = count_vect.fit_transform(doc[:-1] for doc in training_data)

	return X.toarray(), count_vect.vocabulary_

def posgrams3(filename):
	with open(filename,'r') as f:
		data = f.read()

	data = data.decode('utf-8')
	bigram_vectorizer = CountVectorizer(ngram_range=(3,3),token_pattern=r'\b\w+\b', min_df=1)
	analyze = bigram_vectorizer.build_analyzer()

	output = analyze(data)

	training_data = nltk.pos_tag(output)

	# print training_data

	count_vect = CountVectorizer(preprocessor=lambda x:x,tokenizer=lambda x:x)
	
	X = count_vect.fit_transform(doc[:-1] for doc in training_data)

	return X.toarray(), count_vect.vocabulary_
