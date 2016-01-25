from nltk import tag
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# We need to be able to use this to extract all the n-grams from the text, n=1,2,3
# We also need to get a general n-grams set, n=1,2,3

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
