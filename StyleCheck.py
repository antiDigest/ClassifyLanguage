from nltk import tag
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# We need to be able to use this to extract all the n-grams from the text, n=1,2,3
# We also need to get a general n-grams set, n=1,2,3

def posgrams(filename):
	with open(filename,'r') as f:
		data = f.read()

	data = data.decode('utf-8')
	bigram_vectorizer = CountVectorizer(ngram_range=(1,3),token_pattern=r'\b\w+\b', min_df=1)
	analyze = bigram_vectorizer.build_analyzer()

	output = analyze(data)

	# print output

	training_data = nltk.pos_tag(output)

	# count_vect = CountVectorizer(preprocessor=lambda x:x,tokenizer=lambda x:x)
	
	# X = count_vect.fit_transform(doc[:-1] for doc in training_data)

	# print json.dumps(dict(training_data),sort_keys=True,indent=4, separators=(',', ': '))

	return dict(training_data)

def tense(text):

	text = posgrams(text)

	past = ['VBD', 'VBN']
	past_brown = ['WDT+DOD', 'WPS+HVD', 'VBD', 'DOD*', 'PPSS+HVD', 'NN+HVD', 'BEN', \
	'BED', 'WRB+DOD', 'EX+HVD', 'BEDZ', 'BED*', 'VBN+TO', 'FW-VBN', 'VBN', 'DOD', 'BEDZ*', \
	'DO+PPSS', 'HVN', 'HVD', 'FW-VBD', 'WRB+DOD*', 'AP', 'HVD*', 'PPS+HVD', 'PN+HVD']
	past_claws = ['VBD', 'VBN', 'VDD', 'VDN', 'VHD', 'VVN', 'VVD', 'VHN']
	pres = ['VBG','VBP','VBZ']
	pres_brown = ['VBG+TO', 'WPS+HVZ', 'BEZ*', 'WRB+BER', 'NP+HVZ', 'WRB+BEZ', 'WPS+BEZ', 'PPSS+BER',\
	 'PPSS+BEM', 'NNS', 'FW-DT+BEZ', 'PN+HVZ', 'HVZ*', 'VB+AT', 'PPS+HVZ', 'BEM', 'EX+BEZ', 'HV',\
	  'BEG', 'BEZ', 'BER', 'DTS+BEZ', 'NN+HVZ', 'BEM*', 'FW-BEZ', 'EX+HVZ', 'FW-BER', 'NP+BEZ', 'BER*',\
	   'PPSS+BEZ', 'VBZ', 'VB+JJ', 'PPS+BEZ', 'HV*', 'VBG', 'DOZ', 'FW-PPSS+HV', 'WDT+DO+PPS', 'FW-HV',\
	    'WRB+DOZ', 'WDT+BER', 'WDT+BEZ', 'DT+BEZ', 'DO+PPSS', 'DO*', 'WRB+DO', 'FW-VBZ', 'HVG', 'HVZ',\
	     'VB+TO', 'FW-VBG', 'DO', 'VB+VB', 'RB+BEZ', 'VB+IN', 'WDT+BER+PP', 'FW-VB', 'PN+BEZ', \
	     'PPSS+BEZ*', 'FW-PPL+VBZ', 'WDT+HVZ', 'NN+BEZ', 'PPSS+VB', 'VB+PPO', 'VB', 'AP', 'PPSS+HV', \
	     'DOZ*', 'HV+TO']

	for key in text.keys():
		print key