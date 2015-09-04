from nltk import tag
from sklearn.feature_extraction.text import CountVectorizer

# def BrillTag(filename):

def posgrams1(filename):
	with open(filename,'r') as f:
		data = f.read() 

	

	count_vect = count_vect = CountVectorizer(preprocessor=lambda x:x,tokenizer=lambda x:x)
	
	X = count_vect.fit_transform(doc[:-1] for doc in training_data)

	return X.toarray(), count_vect.vocabulary_
	